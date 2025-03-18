import os
import requests
from dotenv import load_dotenv

def post_to_wix(content):
    """
    Posta o 'content' gerado no Wix Blog, criando um RASCUNHO
    via a Draft Posts API.
    """
    load_dotenv()

    # Pega as credenciais do Wix no .env
    wix_access_token = os.getenv("WIX_ACCESS_TOKEN")
    wix_site_id = os.getenv("WIX_SITE_ID")

    if not wix_access_token or not wix_site_id:
        raise Exception("Credenciais do Wix não configuradas. "
                        "Defina WIX_ACCESS_TOKEN e WIX_SITE_ID no .env")

    # Endpoint oficial para criar rascunhos de posts
    url = "https://www.wixapis.com/blog/v1/draft-posts"

    # Exemplo simples: usando 'richContent' (recomendado na doc).
    # Vamos usar 'content' do Mercury como texto principal,
    # mas se quiser, pode gerar título dinamicamente.
    payload = {
        "title": "Post gerado pelo Mercury",
        "excerpt": "Postagem curta gerada automaticamente",
        "commentingEnabled": True,
        "featured": False,
        "richContent": {
            "nodes": [
                {
                    "type": "PARAGRAPH",
                    "nodes": [
                        {
                            "type": "TEXT",
                            "textData": {
                                "text": content
                            }
                        }
                    ]
                }
            ]
        }
    }

    headers = {
        "Authorization": f"Bearer {wix_access_token}",
        "Content-Type": "application/json",
        "wix-site-id": wix_site_id
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code in [200, 201]:
        print("Rascunho criado com sucesso no Wix:")
        print(response.json())
    else:
        print(f"Erro ao criar rascunho no Wix (status {response.status_code}):")
        print(response.text)

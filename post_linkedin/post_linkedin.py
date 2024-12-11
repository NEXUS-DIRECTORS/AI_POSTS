import requests
import json

# Configurações do LinkedIn
access_token = "SEU_ACCESS_TOKEN"
headers = {"Authorization": f"Bearer {access_token}"}

# Carregar textos e imagens gerados
with open('data/generated_texts.json', 'r', encoding='utf-8') as f:
    generated_texts = json.load(f)

with open('data/generated_images.json', 'r', encoding='utf-8') as f:
    generated_images = json.load(f)

# Combinar texto e imagem para postar
for text, image in zip(generated_texts, generated_images):
    post_data = {
        "author": "urn:li:person:SEU_URN",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text['text']
                },
                "shareMediaCategory": "IMAGE",
                "media": [
                    {
                        "status": "READY",
                        "originalUrl": image['image_url']
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    # Enviar para o LinkedIn
    response = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        headers=headers,
        json=post_data
    )

    if response.status_code == 201:
        print(f"Postagem criada com sucesso para o tópico: {text['title']}")
    else:
        print(f"Erro ao criar postagem: {response.status_code}, {response.text}")

# AI_agents/mercury_agent.py

import re
import os
import json
import random
import google.generativeai as genai
from dotenv import load_dotenv

def generate_mercury_post(reddit_file_path):
    """
    Lê os tópicos do arquivo reddit_file_path, seleciona um post (preferencialmente com 'crypto' no título),
    gera uma postagem noticiosa utilizando o agente Mercury via Gemini e remove o post utilizado do arquivo.
    """
    load_dotenv()
    
    # Configurar a API do Gemini
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise Exception("GEMINI_API_KEY não configurado no ambiente.")
    genai.configure(api_key=gemini_api_key)
    
    # Configuração do modelo Gemini
    generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
    )
    
    # Carregar os posts do arquivo JSON
    with open(reddit_file_path, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    
    if not posts:
        raise Exception("Nenhum post disponível no arquivo JSON.")
    
    # Filtrar posts que contenham 'crypto' no título (caso exista)
    filtered_posts = [post for post in posts if "crypto" in post.get("title", "").lower()]
    
    if filtered_posts:
        chosen_post = random.choice(filtered_posts)
    else:
        chosen_post = random.choice(posts)
    
    # Montar o prompt para o agente Mercury
    prompt = f"""
Você é o Mercury SEO, um agente de IA especializado em criar conteúdo jornalístico otimizado para mecanismos de busca, focado no universo das criptomoedas para a comunidade "Flash Crypto".  
Sua tarefa é desenvolver uma postagem noticiosa exclusiva e original, totalmente orientada para SEO, que aborde as últimas novidades e atualizações do mundo cripto. Utilize os seguintes dados como inspiração:

Título: {chosen_post['title']}  
Conteúdo: {chosen_post.get('selftext', '')}  
URL: {chosen_post.get('url', '')}  

Crie uma notícia otimizada para SEO com os seguintes elementos:
- Inicie com um parágrafo `<p>` resumo que resuma a notícia e inclua palavras-chave estratégicas para melhorar o ranking nos motores de busca.
- Estruture o conteúdo com subtítulos utilizando `<h2>` e `<h3>` para facilitar a leitura e a indexação, separando diferentes seções informativas.
- Insira meta descrições, atribuições alt para imagens (caso inclua imagens) e links internos/externos pertinentes para enriquecer o SEO da página.
- Desenvolva um texto jornalístico que apresente os fatos, dados relevantes e contexto sobre o tema, mantendo o tom informativo e original, sem copiar literalmente o conteúdo fornecido.
- Evite exageros na repetição das palavras-chave (keyword stuffing) e mantenha a naturalidade e fluidez do texto.

Por favor, gere um JSON válido no seguinte formato:
{{
  "title": "Texto do título (sem tags HTML)",
  "html": "Conteúdo da notícia em HTML, com tags, parágrafos e subtítulos se necessário"
}}

    """
    # Dividir em prompt de sistema e prompt de usuário(o que é variável)

    # Iniciar a sessão de chat com o modelo Gemini
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    output_text = response.text.strip()
    output_text = re.sub(r'```(json)?', '', output_text)
    output_text = re.sub(r'```', '', output_text)
    # Tentar interpretar a resposta como JSON
    try:
        mercury_output = json.loads(output_text)
    except Exception as e:
        # Se ocorrer erro, retorne um fallback com o conteúdo inteiro como HTML e um título genérico
        mercury_output = {
            "title": "Notícia do Mercury",
            "html": output_text
        }
    
    # Remover o post utilizado para evitar reutilização
    remaining_posts = [post for post in posts if post != chosen_post]
    with open(reddit_file_path, 'w', encoding='utf-8') as file:
        json.dump(remaining_posts, file, ensure_ascii=False, indent=4)
    
    return mercury_output

if __name__ == "__main__":
    reddit_file = "data/api_connector_reddit_content.json"
    generated_post = generate_mercury_post(reddit_file)
    print("Postagem gerada pelo agente Mercury:")
    print(json.dumps(generated_post, indent=4, ensure_ascii=False))

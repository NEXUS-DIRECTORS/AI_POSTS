# AI_agents/mercury_agent.py

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
        model_name="gemini-1.5-flash-8b",
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
Você é o Mercury, um agente de IA especialista em notícias do mundo cripto para a comunidade "Flash Crypto". 
Sua tarefa é criar uma postagem noticiosa que aborde as últimas novidades do universo das criptomoedas e não ultrapassse de nenhuma forma 280 caracteres. 
Utilize o seguinte tópico e texto como inspiração:

Título: {chosen_post['title']}
Conteúdo: {chosen_post.get('selftext', '')}

Crie uma notícia bem estruturada com os seguintes elementos:
- Um título chamativo e informativo.
- Um texto jornalístico que introduza os fatos, apresente dados relevantes e contextualize as informações, mantendo o tom informativo e original.

A notícia deve ser única, utilizando os dados do post apenas como inspiração, sem copiar literalmente o conteúdo.
O output deve ter no máximo 280 caracteres e ser escrito em TXT puro!!!!
    """
    
    # Iniciar a sessão de chat com o modelo Gemini
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    mercury_post = response.text.strip()
    
    # Remover o post utilizado para evitar reutilização
    remaining_posts = [post for post in posts if post != chosen_post]
    with open(reddit_file_path, 'w', encoding='utf-8') as file:
        json.dump(remaining_posts, file, ensure_ascii=False, indent=4)
    
    return mercury_post

if __name__ == "__main__":
    reddit_file = "data/api_connector_reddit_content.json"
    generated_post = generate_mercury_post(reddit_file)
    print("Postagem gerada pelo agente Mercury:")
    print(generated_post)

import openai
import json
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurar a chave da API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Caminho dos arquivos
input_file = 'data/filter_reddit.json'
output_file = 'data/generated_texts.json'

# Carregar os tópicos filtrados
try:
    with open(input_file, 'r', encoding='utf-8') as f:
        filtered_posts = json.load(f)
except FileNotFoundError:
    print(f"Arquivo {input_file} não encontrado.")
    exit()

# Verificar se há tópicos para processar
if not filtered_posts:
    print("Nenhum tópico encontrado no arquivo de entrada.")
    exit()

# Lista para armazenar os textos gerados
generated_texts = []

print("Iniciando a geração de textos...")
for index, post in enumerate(filtered_posts):
    try:
        # Criar o prompt para o modelo
        prompt = f"Crie um texto profissional para LinkedIn baseado no seguinte tópico:\n\nTítulo: {post['title']}\nDescrição: {post.get('selftext', 'Sem descrição disponível.')}\n"

        # Fazer a chamada à API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ou use "gpt-3.5-turbo" se preferir
            messages=[
                {"role": "system", "content": "Você é um assistente especializado em criar textos para LinkedIn."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )

        # Extrair o texto gerado
        generated_text = response['choices'][0]['message']['content'].strip()
        generated_texts.append({
            "title": post['title'],
            "text": generated_text
        })

        print(f"[{index + 1}/{len(filtered_posts)}] Texto gerado com sucesso para o tópico: {post['title']}")

    except Exception as e:
        print(f"Erro ao gerar texto para o tópico '{post['title']}': {e}")

# Salvar os textos gerados em um arquivo JSON
try:
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(generated_texts, f, ensure_ascii=False, indent=4)
    print(f"Textos gerados foram salvos em '{output_file}'.")
except Exception as e:
    print(f"Erro ao salvar os textos gerados: {e}")

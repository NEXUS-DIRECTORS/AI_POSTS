from dotenv import load_dotenv
import praw
import os
import json

# Carregar variáveis de ambiente
load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent='NexusTrendCollector by /u/SeuNomeDeUsuário',
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD')
)

# Verifica se a instância está em modo somente leitura
print("Modo somente leitura:", reddit.read_only)

subreddits = ['technology', 'MachineLearning', 'artificial', 'automation', 'Futurology', 'tech']
top_posts = []

# Coletar posts de subreddits
for subreddit_name in subreddits:
    print(f"Acessando o subreddit: {subreddit_name}")
    try:
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=50):
            top_posts.append({
                'title': post.title,
                'score': post.score,
                'url': post.url,
                'created': post.created_utc,
                'selftext': post.selftext,
                'subreddit': subreddit_name
            })
    except Exception as e:
        print(f"Erro ao acessar o subreddit {subreddit_name}: {e}")

# Mostrar os posts coletados
if top_posts:
    print(f"Número de posts coletados: {len(top_posts)}")
else:
    print("Nenhum post foi coletado. Verifique os subreddits ou filtros aplicados.")

# Filtrar posts por relevância
palavras_chave = ['AI', 'inteligência artificial', 'automação', 'tecnologia', 'machine learning', 'robótica', 'inovação']
pontuacao_minima = 100

posts_filtrados = []

for post in top_posts:
    if any(palavra.lower() in post['title'].lower() for palavra in palavras_chave):
        if post['score'] >= pontuacao_minima:
            posts_filtrados.append(post)

# Mostrar os posts filtrados
if posts_filtrados:
    print(f"Número de posts filtrados: {len(posts_filtrados)}")
else:
    print("Nenhum post passou pelos filtros. Verifique as palavras-chave ou a pontuação mínima.")

# Salvar os posts filtrados no arquivo JSON dentro da pasta 'data'
output_file = 'data/filter_reddit.json'
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(posts_filtrados, f, ensure_ascii=False, indent=4)

print(f"Os posts filtrados foram salvos em '{output_file}'.")

# Leitura de dados para testar o fluxo
with open(output_file, 'r', encoding='utf-8') as f:
    filtered_posts = json.load(f)

if filtered_posts:
    print(f"Preparado para o próximo módulo. Número de posts filtrados: {len(filtered_posts)}")
    print("Exemplo de post preparado:")
    print(f"Título: {filtered_posts[0]['title']}")
    print(f"Descrição: {filtered_posts[0]['selftext']}")
    print(f"URL: {filtered_posts[0]['url']}")

    # Exemplo de integração com geração de texto
    print("\nPronto para gerar texto com base no seguinte tópico:")
    print(f"Título: {filtered_posts[0]['title']}")
    print(f"Descrição: {filtered_posts[0]['selftext']}")

    # Exemplo de integração com geração de imagens
    print("\nPronto para gerar imagem com base no seguinte tópico:")
    print(f"Prompt para imagem: {filtered_posts[0]['title']}")
else:
    print("Nenhum post encontrado no arquivo 'filter_reddit.json'.")

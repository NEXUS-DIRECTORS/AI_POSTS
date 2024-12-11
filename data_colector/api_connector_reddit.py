from dotenv import load_dotenv
import praw
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent='NexusTrendCollector by /u/SeuNomeDeUsuário',  # Substitua pelo seu nome de usuário
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD')
)

# Verifica se a instância está em modo somente leitura
print("Modo somente leitura:", reddit.read_only)

subreddits = ['technology', 'MachineLearning', 'ArtificialIntelligence', 'automation', 'Futurology', 'tech']  # 'technews' removido
top_posts = []

for subreddit_name in subreddits:
    print(f"Acessando o subreddit: {subreddit_name}")
    try:
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=50):
            top_posts.append({
                'title': post.title,
                'score': post.score,
                'url': post.url,
                'num_comments': post.num_comments,
                'created': post.created_utc,
                'selftext': post.selftext,
                'subreddit': subreddit_name
            })
    except Exception as e:
        print(f"Erro ao acessar o subreddit {subreddit_name}: {e}")

palavras_chave = ['AI', 'inteligência artificial', 'automação', 'tecnologia', 'machine learning', 'robótica', 'inovação']
pontuacao_minima = 100  # Ajuste conforme necessário

posts_filtrados = []

for post in top_posts:
    if any(palavra.lower() in post['title'].lower() for palavra in palavras_chave):
        if post['score'] >= pontuacao_minima:
            posts_filtrados.append(post)

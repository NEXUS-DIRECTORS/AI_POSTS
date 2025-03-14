# main_mercury.py

from AI_agents.mercury_agent import generate_mercury_post
from post.post_to_x import post_to_x

def main():
    reddit_file_path = "data/api_connector_reddit_content.json"
    
    # Gerar a postagem com o agente Mercury
    mercury_post = generate_mercury_post(reddit_file_path)
    print("Postagem gerada pelo agente Mercury:")
    print(mercury_post)
    
    # Postar a mensagem gerada no X (Twitter)
    post_to_x(mercury_post)

if __name__ == "__main__":
    main()

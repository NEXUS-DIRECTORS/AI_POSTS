from AI_agents.mercury_agent import generate_mercury_post
from post.post_to_x import post_to_x
from post.post_to_wix import post_to_wix  # <--- ADICIONE ESTA LINHA

def main():
    reddit_file_path = "data/api_connector_reddit_content.json"
    
    # Gerar a postagem com o agente Mercury
    mercury_post = generate_mercury_post(reddit_file_path)
    print("Postagem gerada pelo agente Mercury:")
    print(mercury_post)
    
    # Postar a mensagem gerada no X (Twitter)
    post_to_x(mercury_post)

    # Postar a mesma mensagem no Wix
    post_to_wix(mercury_post)   # <--- CHAME AQUI

if __name__ == "__main__":
    main()

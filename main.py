# main.py

from content_colector.google_sheet_connector import insert_campaign
from AI_agents.hermes_agent import generate_campaign_post
from post.post_to_x import post_to_x

def main():
    # Dados da campanha
    campaign_name = "Airdrop Flash Crypto"
    affiliate_link = "https://exemplo.com/afiliado123"
    announcement_text = (
        "Participe do nosso airdrop e ganhe tokens exclusivos! "
        "Inscreva-se já e aproveite essa oportunidade única."
    )
    
    # 1. Inserir os dados da campanha no Google Sheets
    insert_campaign(campaign_name, affiliate_link, announcement_text)
    
    # 2. Gerar a postagem com o agente Hermes via Gemini
    post_content = generate_campaign_post(campaign_name, affiliate_link, announcement_text)
    print("Postagem gerada pelo agente Hermes:")
    print(post_content)
    
    # 3. Postar a mensagem gerada no X (Twitter)
    post_to_x(post_content)

if __name__ == "__main__":
    main()

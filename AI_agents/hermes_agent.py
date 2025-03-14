# AI_agents/hermes_agent.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

def generate_campaign_post(campaign_name, affiliate_link, announcement_text):
    """
    Gera uma postagem promocional para a campanha utilizando o agente Hermes.
    """
    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise Exception("GEMINI_API_KEY não configurado no ambiente.")
    
    genai.configure(api_key=gemini_api_key)
    
    generation_config = {
        "temperature": 0.6,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-8b",
        generation_config=generation_config,
    )
    
    prompt = f"""
Você é o Hermes, um agente de IA especialista em criar postagens promocionais para campanhas de airdrop na comunidade "Flash Crypto". 
Sua tarefa é criar uma postagem atraente e informativa com base nos dados da campanha abaixo:

Campanha: {campaign_name}
Link de Afiliado: {affiliate_link}
Texto de Anúncio: {announcement_text}

Crie uma postagem que contenha:
- Um título chamativo,
- Um corpo explicativo com informações detalhadas sobre a campanha,
- Um call-to-action para que os usuários participem.

Utilize os dados de forma original e criativa, sem copiar literalmente o texto de anúncio.
    """
    
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    return response.text

if __name__ == "__main__":
    # Exemplo de uso
    campaign_name = "Airdrop Flash Crypto"
    affiliate_link = "https://exemplo.com/afiliado123"
    announcement_text = (
        "Participe do nosso airdrop e ganhe tokens exclusivos! "
        "Inscreva-se já e aproveite essa oportunidade única."
    )
    post_content = generate_campaign_post(campaign_name, affiliate_link, announcement_text)
    print("Postagem gerada pelo agente Hermes:")
    print(post_content)

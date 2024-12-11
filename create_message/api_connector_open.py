import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_linkedin_post(topic: str) -> str:
    prompt = f"""
    Você é um redator de conteúdo para LinkedIn de uma empresa de automação e inteligência artificial chamada Nexus.
    A partir do tópico abaixo, crie um post profissional, conciso e que agregue valor aos leitores:
    
    Tópico: {topic}

    Instruções:
    - Estilo: Profissional, informativo, empolgante
    - Idioma: Português
    - Incluir um call-to-action no final, convidando o leitor a comentar sua opinião.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )

    # A resposta será retornada no campo 'choices'
    message = response.choices[0].message.content.strip()
    return message

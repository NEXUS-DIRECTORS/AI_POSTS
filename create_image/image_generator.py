import json
import openai

# Configurar a API OpenAI (substitua com sua chave API)
openai.api_key = "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"

# Carregar os tópicos filtrados
with open('data/filter_reddit.json', 'r', encoding='utf-8') as f:
    filtered_posts = json.load(f)

# Gerar imagens para os tópicos
generated_images = []

for post in filtered_posts:
    prompt = f"Crie uma imagem representando o tema: {post['title']}"
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    generated_images.append({
        "title": post['title'],
        "image_url": image_url
    })

# Salvar as imagens geradas
with open('data/generated_images.json', 'w', encoding='utf-8') as f:
    json.dump(generated_images, f, ensure_ascii=False, indent=4)

print("URLs das imagens geradas foram salvas em 'data/generated_images.json'.")

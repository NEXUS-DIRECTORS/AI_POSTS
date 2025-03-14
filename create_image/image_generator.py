from PIL import Image, ImageDraw, ImageFont

# Carregar o template base
template = Image.open("C:/Users/carlo/OneDrive/Área de Trabalho/automacao_postagens/AI_POSTS/data/templates/postagem_linkedin.png")

# Criar objeto para edição
draw = ImageDraw.Draw(template)

# Carregar fontes personalizadas
font_title = ImageFont.truetype("C:/Users/carlo/OneDrive/Área de Trabalho/automacao_postagens/AI_POSTS/data/fonts/Montserrat-Bold.ttf", size=60)
font_subtitle = ImageFont.truetype("C:/Users/carlo/OneDrive/Área de Trabalho/automacao_postagens/AI_POSTS/data/fonts/Montserrat-Regular.ttf", size=40)

# Definir os textos
titulo = "Tema da Postagem: Automação Inteligente com IA"
subtitulo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"

# Função para quebrar o texto automaticamente
def quebrar_texto(draw, text, font, largura_maxima):
    palavras = text.split()  # Divide o texto em palavras
    linhas = []
    linha_atual = ""
    
    for palavra in palavras:
        teste_linha = linha_atual + " " + palavra if linha_atual else palavra
        bbox = draw.textbbox((0, 0), teste_linha, font=font)
        largura_texto = bbox[2] - bbox[0]
        if largura_texto <= largura_maxima:
            linha_atual = teste_linha
        else:
            linhas.append(linha_atual)
            linha_atual = palavra
    linhas.append(linha_atual)  # Adiciona a última linha
    return linhas

# Função para desenhar texto centralizado com quebras automáticas
def desenhar_texto_centralizado(draw, text, font, largura_imagem, y_inicial, largura_maxima, line_spacing=10):
    linhas = quebrar_texto(draw, text, font, largura_maxima)
    altura_linha = draw.textbbox((0, 0), "A", font=font)[3] - draw.textbbox((0, 0), "A", font=font)[1]
    y_pos = y_inicial

    for linha in linhas:
        bbox = draw.textbbox((0, 0), linha, font=font)
        text_width = bbox[2] - bbox[0]
        x_pos = (largura_imagem - text_width) // 2  # Centraliza horizontalmente
        draw.text((x_pos, y_pos), linha, fill="white", font=font)
        y_pos += altura_linha + line_spacing  # Incrementa para a próxima linha

# Obter dimensões da imagem
largura, altura = template.size

# Largura máxima para o texto (80% da largura da imagem)
largura_maxima = int(largura * 0.8)

# Adicionar textos centralizados com quebra automática de linha
desenhar_texto_centralizado(draw, titulo, font_title, largura, y_inicial=150, largura_maxima=largura_maxima)
desenhar_texto_centralizado(draw, subtitulo, font_subtitle, largura, y_inicial=300, largura_maxima=largura_maxima)

# Salvar a imagem final
template.save("postagem_final_quebra_linhas.png")

print("Imagem gerada com sucesso!")
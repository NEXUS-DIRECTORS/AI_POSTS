# Flash Crypto Post Automation

Este projeto tem como objetivo automatizar a criação e publicação de conteúdos para a comunidade "Flash Crypto". O sistema integra diversas funcionalidades, como:

- **Cadastro de campanhas de airdrop:** Insere os dados da campanha (nome, link de afiliado e texto de anúncio) em uma planilha do Google Sheets.
- **Geração de postagens com agentes de IA:**  
  - **Agente Hermes:** Cria postagens promocionais para campanhas de airdrop.  
  - **Agente Mercury:** Gera notícias inspiradas em tópicos coletados do Reddit.
- **Publicação no X (Twitter):** Posta o conteúdo gerado utilizando a API v2 com OAuth 1.0a.

---

## Estrutura do Projeto

```
seu_projeto/
├── AI_agents/
│   ├── hermes_agent.py       # Agente Hermes para campanhas de airdrop
│   └── mercury_agent.py      # Agente Mercury para geração de notícias do universo cripto
├── content_colector/
│   └── google_sheet_connector.py  # Conexão com o Google Sheets para cadastro de campanhas
├── data/
│   └── api_connector_reddit.json  # Arquivo com os posts coletados do Reddit
├── post/
│   └── post_to_x.py          # Conexão e postagem no X (Twitter) utilizando a API v2 via OAuth1
├── main.py                   # Fluxo do agente Hermes (Campanhas de Airdrop)
├── main_mercury.py           # Fluxo do agente Mercury (Notícias do Reddit)
└── .env                      # Arquivo de variáveis de ambiente
```

---

## Dependências

O projeto utiliza as seguintes bibliotecas:

- **python-dotenv** (para carregamento de variáveis de ambiente)
- **gspread** (para integração com o Google Sheets)
- **google-generativeai** (para interação com a API do Gemini)
- **requests** e **requests_oauthlib** (para conexão com a API do X via OAuth 1.0a)
- **tweepy** (caso opte por usar outra abordagem para postar no X)

Instale as dependências com:

```bash
pip install python-dotenv gspread google-generativeai requests requests_oauthlib tweepy
```

---

## Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```dotenv
# Google Sheets
GOOGLE_SHEETS_CREDENTIALS=path/to/your/google-credentials.json

# Gemini API (Google Generative AI)
GEMINI_API_KEY=your_gemini_api_key

# X (Twitter) - API v2 com OAuth 1.0a
X_API_KEY=your_twitter_api_key
X_API_SECRET=your_twitter_api_secret
X_ACCESS_TOKEN=your_twitter_access_token
X_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
```

---

## Uso do Projeto

### Fluxo Hermes (Campanhas de Airdrop)

Este fluxo executa os seguintes passos:
1. **Cadastro no Google Sheets:** Insere os dados da campanha (nome, link de afiliado e texto de anúncio) na planilha.
2. **Geração da Postagem:** Utiliza o agente Hermes (via API Gemini) para criar uma postagem promocional.
3. **Postagem no X:** Publica a mensagem gerada no X (Twitter).

Para executar o fluxo Hermes, rode:

```bash
python main.py
```

---

### Fluxo Mercury (Notícias do Universo Cripto)

Este fluxo executa os seguintes passos:
1. **Leitura e Filtragem:** Lê os tópicos do arquivo `data/api_connector_reddit.json` e seleciona um post (preferencialmente relacionado a "crypto").
2. **Geração da Notícia:** Utiliza o agente Mercury (via API Gemini) para gerar uma notícia inspirada no tópico selecionado.
3. **Remoção do Post Utilizado:** Remove o tópico utilizado do arquivo JSON para evitar duplicidades.
4. **Postagem no X:** Publica a notícia no X (Twitter).

Para executar o fluxo Mercury, rode:

```bash
python main_mercury.py
```

---

## Personalizações e Expansões

- **Google Sheets:**  
  - Modifique o nome da planilha ou a aba utilizada em `content_colector/google_sheet_connector.py` se necessário.

- **Agentes de IA (Hermes e Mercury):**  
  - Ajuste os prompts e parâmetros (como `temperature` e `max_output_tokens`) nos arquivos `AI_agents/hermes_agent.py` e `AI_agents/mercury_agent.py` conforme o estilo e a extensão desejada para os textos gerados.
  
- **Postagem no X:**  
  - Se o conteúdo gerado ultrapassar os 280 caracteres permitidos pelo X, considere implementar uma função de truncamento ou dividir o conteúdo em threads.

- **Coleta de Dados do Reddit:**  
  - O arquivo `data/api_connector_reddit.json` deve conter posts coletados do Reddit, com campos como `title`, `selftext` e `subreddit`.

---

## Considerações Finais

- **Credenciais:**  
  Verifique se todas as credenciais e permissões estão corretamente configuradas nas variáveis de ambiente.
  
- **Modularidade:**  
  O projeto foi estruturado de forma modular para facilitar a manutenção e a escalabilidade. Você pode executar e testar cada módulo separadamente antes de orquestrar o fluxo completo.

- **Erros e Logs:**  
  Caso ocorram erros durante a execução, verifique os logs e as mensagens de erro para identificar problemas com credenciais, permissões ou limites de caracteres.

---

## Suporte e Contribuição

Caso tenha dúvidas, sugestões ou encontre algum problema, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

---

Este README fornece uma visão geral do projeto e orientações para configuração e execução dos fluxos. Adapte-o conforme necessário para atender às necessidades do seu projeto "Flash Crypto".
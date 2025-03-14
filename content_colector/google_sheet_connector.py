# content_colector/google_sheet_connector.py

import os
import gspread
from dotenv import load_dotenv

def insert_campaign(campaign_name, affiliate_link, announcement_text):
    """
    Insere os dados da campanha no Google Sheets.
    """
    load_dotenv()
    google_creds_file = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
    if not google_creds_file:
        raise Exception("Arquivo de credenciais do Google Sheets não configurado nas variáveis de ambiente.")
    
    gc = gspread.service_account(filename=google_creds_file)
    # Abre a planilha pelo nome (certifique-se de que a planilha exista)
    spreadsheet = gc.open("Campanhas Airdrop")
    worksheet = spreadsheet.sheet1  # Utiliza a primeira aba
    
    new_row = [campaign_name, affiliate_link, announcement_text]
    worksheet.append_row(new_row)
    print("Dados da campanha inseridos no Google Sheets.")

if __name__ == "__main__":
    # Exemplo de uso
    campaign_name = "Airdrop Flash Crypto"
    affiliate_link = "https://exemplo.com/afiliado123"
    announcement_text = (
        "Participe do nosso airdrop e ganhe tokens exclusivos! "
        "Inscreva-se já e aproveite essa oportunidade única."
    )
    insert_campaign(campaign_name, affiliate_link, announcement_text)

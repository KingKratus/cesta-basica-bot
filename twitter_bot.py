import tweepy
import pandas as pd
import json
import schedule
import time
from datetime import datetime

# Substitua pelos seus dados reais da API do Twitter
API_KEY = "sua_api_key"
API_SECRET = "sua_api_secret"
ACCESS_TOKEN = "seu_access_token"
ACCESS_TOKEN_SECRET = "seu_access_token_secret"

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def load_cesta_basica_data(json_path):
    with open(json_path, 'r') as file:
        cesta_data = json.load(file)
    return cesta_data

def calculate_total_cesta(cesta_data, preco_unitario=10.0):
    """
    Calcula um custo total hipotético da cesta básica.
    Aqui usamos um 'preco_unitario' fictício; ajuste conforme os preços reais.
    """
    total = 0
    for item in cesta_data['itens']:
        total += item['quantidade'] * preco_unitario
    return total

def generate_message(data_path, cesta_json_path):
    data = pd.read_csv(data_path)
    last_row = data.iloc[-1]

    price = last_row['price']
    daily_variation = last_row['daily_variation']
    daily_percentage = last_row['daily_percentage']
    monthly_accumulated = last_row['monthly_accumulated']
    monthly_percentage = last_row['monthly_percentage']

    # Carrega a cesta básica e calcula um custo total (valor hipotético)
    cesta_basica = load_cesta_basica_data(cesta_json_path)
    total_cesta = calculate_total_cesta(cesta_basica)
    
    # Captura a data atual para incluir no tweet
    hoje = datetime.now().strftime("%d/%m/%Y")

    message = (
        f"📊 Data: {hoje}\n"
        f"Hoje o custo da cesta básica é R$ {price:.2f}.\n"
        f"➡️ Variação do dia: R$ {daily_variation:.2f} ({daily_percentage:.2f}%).\n"
        f"📅 Acumulado do mês: R$ {monthly_accumulated:.2f} ({monthly_percentage:.2f}%).\n"
        f"🛒 Custo total estimado da cesta: R$ {total_cesta:.2f}\n"
        f"#CestaBasica"
    )
    return message

def post_tweet():
    try:
        message = generate_message("output/cesta_basica.csv", "data/cesta_basica_nacional.json")
        api.update_status(message)
        print(f"Tweet publicado com sucesso às {datetime.now().strftime('%H:%M:%S')}!")
    except Exception as e:
        print(f"Erro ao publicar tweet: {e}")

def schedule_job():
    # Agenda a execução diária às 8h30
    schedule.every().day.at("08:30").do(post_tweet)

    print("Agendando tweets diariamente às 8h30...")
    while True:
        schedule.run_pending()
        time.sleep(60) # Verifica a cada 60 segundos

if __name__ == "__main__":
    schedule_job()

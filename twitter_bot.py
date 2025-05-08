import tweepy
import pandas as pd

API_KEY = "sua_api_key"
API_SECRET = "sua_api_secret"
ACCESS_TOKEN = "seu_access_token"
ACCESS_TOKEN_SECRET = "seu_access_token_secret"

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def post_tweet(message):
    try:
        api.update_status(message)
        print("Tweet publicado com sucesso!")
    except Exception as e:
        print(f"Erro ao publicar tweet: {e}")

def generate_message(data_path):
    data = pd.read_csv(data_path)
    last_row = data.iloc[-1]

    price = last_row['price']
    daily_variation = last_row['daily_variation']
    daily_percentage = last_row['daily_percentage']
    monthly_accumulated = last_row['monthly_accumulated']
    monthly_percentage = last_row['monthly_percentage']

    message = (
        f"📊 Hoje o custo da cesta básica é R$ {price:.2f}.\n"
        f"➡️ Variação do dia: R$ {daily_variation:.2f} ({daily_percentage:.2f}%).\n"
        f"📅 Acumulado do mês: R$ {monthly_accumulated:.2f} ({monthly_percentage:.2f}%).\n"
        f"🛒 Compare preços e economize mais!"
    )
    return message

if __name__ == "__main__":
    message = generate_message("output/cesta_basica.csv")
    post_tweet(message)

import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

api_key = os.environ.get('alert_key')
secret_key = os.environ.get('alert_secret')

client = Client(api_key, secret_key)


def fetch_data():
    df = client.futures_ticker()
    i = 0
    symbols = []
    while i < len(df):
        percent = float(df[i]['priceChangePercent'])
        if percent > 5.0:
            symbol = df[i]['symbol']
            symbols.append(symbol)
        i += 1
    return symbols



import os

from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


class BinanceClient:

    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise ValueError(
                "API credentials not found. Please configure your .env file."
            )

        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client

    def ping(self):
        try:
            return self.client.futures_ping()
        except Exception as e:
            raise Exception(f"Unable to connect to Binance Testnet: {e}")
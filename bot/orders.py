from binance.exceptions import BinanceAPIException
from requests.exceptions import RequestException

from bot.client import BinanceClient
from bot.logging_config import logger


class OrderManager:

    def __init__(self):
        self.client = BinanceClient().get_client()

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(
                f"MARKET Order Request | Symbol={symbol}, Side={side}, Quantity={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"MARKET Order Response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except RequestException as e:
            logger.error(f"Network Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(
                f"LIMIT Order Request | Symbol={symbol}, Side={side}, Quantity={quantity}, Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"LIMIT Order Response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except RequestException as e:
            logger.error(f"Network Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise
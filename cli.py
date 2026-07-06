import argparse
import sys

from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def print_summary(symbol, side, order_type, quantity, price=None):
    print("\n" + "=" * 45)
    print("        ORDER REQUEST SUMMARY")
    print("=" * 45)
    print(f"Symbol      : {symbol}")
    print(f"Side        : {side}")
    print(f"Order Type  : {order_type}")
    print(f"Quantity    : {quantity}")

    if order_type == "LIMIT":
        print(f"Price       : {price}")

    print("=" * 45)


def print_response(response):
    print("\nOrder Placed Successfully")
    print("-" * 45)
    print(f"Order ID      : {response.get('orderId')}")
    print(f"Status        : {response.get('status')}")
    print(f"Executed Qty  : {response.get('executedQty')}")
    print(f"Average Price : {response.get('avgPrice', 'N/A')}")
    print("-" * 45)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Symbol (Example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"]
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"]
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        price = None

        if order_type == "LIMIT":
            price = validate_price(args.price)

        print_summary(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        manager = OrderManager()

        if order_type == "MARKET":

            response = manager.place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            response = manager.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print_response(response)

    except Exception as e:

        print("\nOrder Failed")
        print("-" * 45)
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
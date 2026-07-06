VALID_SIDES = ["BUY", "SELL"]

VALID_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):

    if not symbol:
        raise ValueError("Symbol cannot be empty")

    return symbol.upper()


def validate_side(side):

    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type):

    order_type = order_type.upper()

    if order_type not in VALID_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity):

    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    return quantity


def validate_price(price):

    if price is None:
        raise ValueError("Price is required for LIMIT order")

    price = float(price)

    if price <= 0:
        raise ValueError("Price must be greater than zero")

    return price
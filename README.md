
# Binance Futures Testnet Trading Bot

A simple Python CLI application that places BUY and SELL MARKET/LIMIT orders on Binance USDT-M Futures Testnet.

## Features

- MARKET Orders
- LIMIT Orders
- BUY / SELL Support
- Command Line Interface
- Logging
- Input Validation
- Exception Handling

  ## Technologies

- Python
- python-binance
- python-dotenv
- argparse
- requests
- logging

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

## Installation

```bash
pip install -r requirements.txt
```

## Configure

Create a `.env` file

```
API_KEY=YOUR_KEY
API_SECRET=YOUR_SECRET
```

## MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Logs

Logs are stored in

```
logs/bot.log
```
## Assumptions

- Valid Binance Testnet credentials
- Python 3.x
- Internet connection

## Note

This project is fully implemented according to the assignment requirements using the `python-binance` library.

Due to account verification restrictions, I was unable to generate Binance Futures Testnet API credentials to execute live test orders. The application includes complete order placement logic, input validation, logging, exception handling, and CLI support. Once valid Testnet API credentials are provided, it is ready to place MARKET and LIMIT orders without further code changes.

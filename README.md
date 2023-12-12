# Crypto Price Monitor

This Python script monitors cryptocurrency prices on Binance and sends a Telegram message when there's a significant price change.

## Prerequisites

Before using this script, make sure you have the following installed:

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`)

## Configuration

1. Obtain a Telegram bot token: [Telegram BotFather](https://core.telegram.org/bots#botfather)
2. Replace the `your_bot_token` variable in the script with your actual Telegram bot token.

```python
your_bot_token = 'your_actual_bot_token'
```

Adjust the tnode dictionary to set the percentage change threshold for each cryptocurrency.
```python
tnode = {
    'BTCUSDT': 0.003,
    'ETHUSDT': 0.005,
    # Add other cryptocurrencies and their threshold values
}
```
Replace the chat_id variable with the actual chat ID where you want to receive notifications.
```python
chat_id = '@YourTelegramChannel'
```
# Usage
## Run the script:
python your_script.py

The script will continuously monitor the specified cryptocurrencies and send a Telegram message when a significant price change is detected.

# Supported Cryptocurrencies
BTCUSDT
ETHUSDT
BNBUSDT
LTCUSDT
ADAUSDT
DOTUSDT
TRXUSDT
XRPUSDT
SOLUSDT
AVAXUSDT
MATICUSDT
MATICBTC


Make sure to replace placeholders such as `your_actual_bot_token` and `@YourTelegramChannel` with your real values. If you haven't chosen a license, you can omit the license section or add the appropriate license information.





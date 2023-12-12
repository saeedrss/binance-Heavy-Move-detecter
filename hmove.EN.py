import requests
import json
import time

chat_id='@MarKetHeavyMove'


your_bot_token=''


TSMurl = f"https://api.telegram.org/bot{your_bot_token}/sendMessage"

def get_last_price(symbol='BTCUSDT'):
    if symbol is not None:
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    else:
        url = f'https://api.binance.com/api/v3/ticker/price?symbol=MATICUSDT'
    try:
        data = requests.get(url).text
        dictionary = json.loads(data)
        if float(dictionary["price"]) > 0:
            return float(dictionary["price"])
        else:
            return None
    except:
        return None

def compare_numbers(num1, num2, threshold=0.004):
    if threshold is None or threshold == 0:
        threshold = 0.004

    if num2 == 0:
        return False
    if abs(num1 - num2) / ((num1 + num2) / 2) > threshold:
        return True
    else:
        return False

def get_message(symbol, last_price, current_price, elapsed_time):
    change = ((current_price - last_price) / abs(last_price)) * 100
    message = f'''
    {symbol}:
    Previous Price: {last_price}
    Current Price: {current_price}
    Percentage Change: {change:.2f}%
    Elapsed Time: {int(elapsed_time)} seconds 
    @MarKetHeavyMove
    '''
    return message

def send_telegram_message(chat_id, text):
    url = TSMurl
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    try:
        with requests.get(url) as response:
            data = response.text
    except requests.exceptions.RequestException as e:
        print(e)

currencies = [
    'BTCUSDT',
    'ETHUSDT',
    'BNBUSDT',
    'LTCUSDT',
    'ADAUSDT',
    'DOTUSDT',
    'TRXUSDT',
    'XRPUSDT',
    'SOLUSDT',
    'AVAXUSDT',
    'MATICUSDT',
    'MATICBTC',
]
threshold_nodes = {}
for i in currencies:
    threshold_nodes[i] = 0.005

price_list = {}
for i in currencies:
    p = get_last_price(i)
    price_list[i] = {'price': p, 'time': time.time()}

T = True
while T:
    for i in currencies:
        p = get_last_price(i)
        t = time.time()
        if compare_numbers(p, price_list[i]['price'], threshold_nodes[i]):
            msg = get_message(i, price_list[i]['price'], p, t - price_list[i]['time'])
            print(msg)
            tdata = {'chat_id': chat_id, 'text': msg}
            response = requests.post(TSMurl, data=tdata)
        price_list[i] = {'price': p, 'time': t}
    time.sleep(27)


import requests
import json
import time

import datetime
chat_id='@MarKetHeavyMove'
now = datetime.datetime.now()

your_bot_token=''
TSMurl = f"https://api.telegram.org/bot{your_bot_token}/sendMessage"


def getlastPrice(syambol='BTCUSDT'):
    if syambol is not None:
        url=f'https://api.binance.com/api/v3/ticker/price?symbol={syambol}'
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


def compare_numbers(num1, num2,p=0.004):
    if p is None or p == 0:
        p = 0.004

    if num2 == 0 :
        return False
    if abs(num1 - num2) / ((num1 + num2) / 2) > p:
        return True
    else:
        return False

def getmsg(symbol, last_price, current_price, elapsed_time):
    change = ((current_price - last_price) / abs(last_price)) * 100
    msg = f'''
    {symbol}:
    قیمت قبلی: {last_price}
    قیمت جدید: {current_price}
    درصد تغییرات: {change:.2f}%
    مدت زمان: {int(elapsed_time)} ثانیه 
    @MarKetHeavyMove
    '''
    return msg

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
tnode={}
for i in currencies:
    tnode[i]= 0.005
tnode['BTCUSDT'] = 0.003
tnode['AVAXUSDT'] = 0.006


pricelist={}
for i in currencies:
    p=getlastPrice(i)
    pricelist[i]= {'price':p,'time':time.time()}


T = True
while T:

    for i in currencies:
        p = getlastPrice(i)
        t= time.time()
        if compare_numbers(p, pricelist[i]['price'],tnode[i]):
            msg = getmsg(i,pricelist[i]['price'],p,t-pricelist[i]['time'])
            print(msg)
            tdata = {'chat_id': chat_id, 'text': msg}
            response = requests.post(TSMurl, data=tdata)

        pricelist[i] = {'price': p, 'time': t}
    time.sleep(27)

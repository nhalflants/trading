import json
import requests
from config import *

BASE_URL = "https://paper-api.alpaca.markets"
HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": "AAPL",
        "qty": 1,
        "side": "buy",
        "type": "market",
        "time_in_force": "gtc"
    }


    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(r.content)

# response = create_order("AAPL", 1, "buy", "market", "gtc")
# response = get_orders()

# print(response)

data = {
    "symbol": "AAPL",
    "qty": 1,
    "side": "buy",
    "type": "market",
    "time_in_force": "gtc",
    "order_class": "bracket",
    "take_profit": {
        "limit_price": "200"
    },
    "stop_loss": {
        "stop_price": "100",
        "limit_price": "100"
    }

}
r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
response = json.loads(r.content)
print(response)
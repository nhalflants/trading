import config
import websocket, json
import dateutil.parser
import sys

minutes_processed = {}
minute_candlesticks = []
current_tick = None
previous_tick = None
in_position = False

def place_order(profit_price, loss_price):
    pass

def on_open(ws):
    # Subscribe to ticker channel to receive feed message
    subscribe_message = {
        "type": "subscribe",
        "channels": [
            {
                "name": "ticker",
                "product_ids": [
                    "ETH-BTC",
                    "ETH-USD"
                ]
            }
        ]
    }
    ws.send(json.dumps(subscribe_message))

def on_message(ws, message):
    global current_tick, previous_tick
    
    previous_tick = current_tick
    current_tick = json.loads(message)
    
    print("*** Received tick ***")
    print("{} - {}".format(current_tick["time"], current_tick["price"]))

    tick_datetime = dateutil.parser.parse(current_tick["time"])
    tick_dt = tick_datetime.strftime("%d/%m/%Y %H:%M")
    print(tick_dt)

    if not tick_dt in minutes_processed:
        print("Starting new candlestick")
        minutes_processed[tick_dt] = True
        print(minutes_processed)

        if len(minute_candlesticks) > 0:
            minute_candlesticks[-1]["close"] = previous_tick["price"]

        minute_candlesticks.append({
            "minute": tick_dt,
            "open": current_tick["price"],
            "high": current_tick["price"],
            "low": current_tick["price"]
        })

    if (len(minute_candlesticks) > 0):
        current_candlestick = minute_candlesticks[-1]
        if current_tick["price"] > current_candlestick["high"]:
            current_candlestick["high"] = current_tick["price"]
        if current_tick["price"] < current_candlestick["low"]:
            current_candlestick["low"] = current_tick["price"]

        print("*** Candlestick ***")
        for candlestick in minute_candlesticks:
            print(candlestick)

        if len(minute_candlesticks) > 3:
            print("*** There are more than 3 candlesticks, checking for pattern ***")
            last_candle = minute_candlesticks[-2]
            previous_candle = minute_candlesticks[-3]
            first_candle = minute_candlesticks[-4]

            print("*** Compare latest 3 candles closes ***")
            
            if last_candle["close"] > previous_candle["close"] and previous_candle["close"] > first_candle["close"]:
                print("*** Three green candelsticks in a row; white soldiers pattern detected ***")
                distance = last_candle["close"] - first_candle["open"]
                profit_price = last_candle["close" + (distance * 2)]
                loss_price = first_candle["open"]
                print(f"Distance is {distance} - Bracket order <profit price:{profit_price} - loss price:{loss_price}")

                if not in_position:
                    in_position = True
                    place_order()
                    sys.exit()

def on_close(ws, close_status_code, close_msg):
    pass

socket = "wss://ws-direct.sandbox.exchange.coinbase.com"

websocket.enableTrace(True)
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()
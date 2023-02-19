def is_bullish_candlestick(candle):
    return float(candle["Close"] > candle["Open"])

def is_bearish_candlestick(candle):
    return float(candle["Close"] < candle["Open"])

def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bearish_candlestick(previous_day) \
        and float(current_day["Close"]) > float(previous_day["Open"]) \
        and float(current_day["Open"]) < float(previous_day["Close"]):
        return True
    
    return False

def is_bearish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bullish_candlestick(previous_day) \
        and current_day["Open"] > previous_day["Close"] \
        and current_day["Close"] < previous_day["Open"]:
        return True
    
    return False
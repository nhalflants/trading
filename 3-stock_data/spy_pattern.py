import csv
from patterns import *

with open("sp500_companies.csv") as f:
    sp500_companies = list(csv.reader(f))

for company in sp500_companies:
    ticker, company_name = company

    with open("history/{}.csv".format(ticker)) as f:
        reader = csv.DictReader(f)
        candles = list(reader)

    candles = candles[-2:]

    if len(candles) > 1:
        if is_bullish_engulfing(candles, 1):
            print("{} - {} is bullish engulfing".format(ticker, candles[1]["Date"]))

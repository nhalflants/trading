import yfinance as yf
import csv

with open("sp500_companies.csv") as f:
    companies = list(csv.reader(f))

for company in companies:
    symbol, name = company
    print(symbol)
    history_filename = "history/{}.csv".format(symbol)

    ticker = yf.Ticker(symbol)
    df = ticker.history(period="1y")
    
    with open(history_filename, "w") as f:
        f.write(df.to_csv())
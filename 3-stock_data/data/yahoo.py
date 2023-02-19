import yfinance as yf

slack = yf.Ticker("AAPL")
history = slack.history(period="1y")
history.to_csv("aapl.csv")
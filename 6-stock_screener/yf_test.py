import yahooquery as yf

msft = yf.Ticker("MSFT")

# get all stock info (slow)
print(msft.summary_detail)



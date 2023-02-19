import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("stock.csv")

candlesticks = go.Candlestick(
    x=df["Date"], 
    open=df["Open"], 
    close=df["Close"],
    high=df["High"], 
    low=df["Low"])

figure = go.Figure(data=[candlesticks])

# ignore weekends
figure.layout.xaxis.type = 'category'

figure.show()

figure.write_html('aapl.html', auto_open=False)
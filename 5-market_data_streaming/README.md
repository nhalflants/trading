# Building an Automated Trading Bot with Python and Real-Time Market Data over Websockets

```
npm install -g wscat
```

```
wscat -c wss://alpaca.socket.polygon.io/stocks
```

```
{"action":"auth","params":"*******"}
```

```
{"action":"subscribe","params":"T.AAPL"}
```

## Steps

* Connect to real time data feed over Websockets
* Process tick data and aggregate/convert the data to real-time price data to OHLC minute candlesticks to keep track of a list of candlesticks
* Process the candlesticks list and detect pattern to execute trades based on price pattern. Use an actual broker (Alpaca) to place trade

* we switch over to using real-time stock market data from Polygon.io for Apple ($AAPL) stock. As real-time bid and ask prices are received over websockets, we build OHLC minute candlesticks and scan them for a bullish pattern. When a bullish pattern is detected, we place a bracket order using the Alpaca API, which allows us to enter a position while also setting profit taking price and stop loss price. In a follow up video, we will refine this strategy to achieve a better signal and outcome.
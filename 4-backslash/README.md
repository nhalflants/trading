# Algorithmic Trading with Python and Backtrader

Use of Backtrader, a Python framework for writing reusable trading strategies and backtesting them against historical data.

## Setup 

1. Install and initialize Backtrader : `pip install backtrader`
2. Connect data feed to python Backtrader
3. Implement trading strategy to define buy and sell orders
4. Define trading signals : Golden Cross (bullish signal) and Death Cross (bearish signal)
5. Calculate the 50 Day and 200 Day Simple Moving Average for SPY
6. Implement a strategy runner that loads different different strategy classes allowing to comparing the result

## Fear and Greed - Backtesting a VIX Spike Trading Strategy with Python

* Volatility Index (the VIX) as a measurement of fear : measure of stock market fear (measure of volatility)

* We backtest our hypothesis that spikes in the VIX above 35 represent good buying opportunities. We show that it has been a profitable strategy to buy when fear rises. What is unclear is if we can time when to sell stocks after buying. We compare a strategy of selling when the VIX drops below a certain threshold vs. a strategy where we never sell and add cash between spikes.

YouTube : https://www.youtube.com/watch?v=UNkH1TQl7qo

## Golden Cross Algorithmic Trading Strategy 
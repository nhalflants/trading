import backtrader as bt

class BuyHold(bt.Strategy):
    def next(self):
        if not self.position:
            size = int(self.broker.getcash() / self.data)
            self.buy(size=size)

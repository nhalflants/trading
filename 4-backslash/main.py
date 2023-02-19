import backtrader
import datetime
from strategies.test_strategy import TestStrategy

cerebro = backtrader.Cerebro()

# Setting the cash
cerebro.broker.set_cash(1000000)

# Load and Inject a Data Feed
## Create Data Feed
data = backtrader.feeds.YahooFinanceCSVData(
    dataname="data/oracle.csv",
    fromdate=datetime.datetime(2000, 1, 1),
    todate=datetime.datetime(2000, 12, 31),
    reverse=False
)

## Add the Data Feed to Cerebro
cerebro.adddata(data)

# Add a strategy
cerebro.addstrategy(TestStrategy)

cerebro.addsizer(backtrader.sizers.FixedSize, stake=1000)

print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())

cerebro.run()

print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())

cerebro.plot()
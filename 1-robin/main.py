import click
import json
import helper
import robin_stocks as rh

@click.group()
def main():
    print("Login in to Robinhood API")
    # content = open("config.json").read()
    # config = json.loads(content)

    # rh.robinhood.authentication.login(config["username"], config["password"])

@main.command(help="Get stock quotes for one or more symbols")
@click.argument("symbols", nargs=-1)
def quote(symbols):
    quotes = rh.robinhood.stocks.get_quotes(symbols)

    for quote in quotes:
        print("{} - {}".format(quote["symbol"], quote["ask_price"]))

@main.command(help="Get stock quotes for watchlist")
def watchlist():
    print("Getting quotes for watchlist")
    with open("watchlist.txt", "r") as f:
        print(f.read().splitlines())

@main.command(help="Buy quantity of stock by symbol")
@click.argument("quantity", type=click.INT)
@click.argument("symbol", type=click.STRING)
@click.option("--limit", type=click.FLOAT)
def buy(quantity, symbol, limit):
    if limit is not None:
        helper.success("Buying {} of {} at {}".format(quantity, symbol, limit))
        result = rh.robinhood.order_buy_limit(symbol, quantity, limit)
    else:
        helper.success("Buying {} of {} at market price".format(quantity, symbol))
        result = rh.robinhood.order_buy_market(symbol, quantity)
    
    if "ref_id" in result:
        helper.success(result)
    else:  
        helper.error(result)

@main.command(help="Sell quantity of stock by symbol")
@click.argument("quantity", type=click.INT)
@click.argument("symbol", type=click.STRING)
@click.option("--limit", type=click.FLOAT)
def sell(quantity, symbol, limit):
    if limit is not None:
        helper.success("Selling {} of {} at {}".format(quantity, symbol, limit))
        result = rh.robinhood.order_sell_limit(symbol, quantity, limit)
    else:
        helper.success("Selling {} of {} at market price".format(quantity, symbol))
        result = rh.robinhood.order_sell_market(symbol, quantity)
    
    if "ref_id" in result:
        helper.success(result)
    else:  
        helper.error(result)

if __name__ == "__main__":
    main()
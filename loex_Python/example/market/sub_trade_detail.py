from loex.client.market import MarketClient


def callback(trade_event):
    print(trade_event)



market_client = MarketClient(init_log=True)
market_client.sub_trade_detail("btcusdt", callback)


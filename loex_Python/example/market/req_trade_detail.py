from loex.client.market import MarketClient



def callback(trade_req):
    print(trade_req)



market_client = MarketClient(init_log=True)
market_client.req_trade_detail("btcusdt", callback)



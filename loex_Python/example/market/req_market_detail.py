from loex.client.market import MarketClient
from loex.model.market import *



def callback(obj_event):
    print(obj_event)


sub_client = MarketClient(init_log=True)
sub_client.req_market_detail("btcusdt", callback)

from loex.client.market import MarketClient
from loex.model.market import *


def callback(obj_event):
    print(obj_event)


market_client = MarketClient(init_log=True)
market_client.sub_market_detail("", callback)
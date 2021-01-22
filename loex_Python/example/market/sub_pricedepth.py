
from loex.client.market import MarketClient
from loex.constant import *



def callback(price_depth_event):
    print(price_depth_event)


def error(e: 'LoexApiException'):
    print(e.error_code + e.error_message)


market_client = MarketClient(init_log=True)
market_client.sub_pricedepth("btcusdt", DepthStep.STEP0, callback, error)

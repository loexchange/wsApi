from loex.client.market import MarketClient
from loex.constant import *
from loex.exception.loex_api_exception import LoexApiException

def callback(candlestick_req):
    print(candlestick_req)

def error(e: 'LoexApiException'):
    print(e.error_code + e.error_message)

sub_client = MarketClient(init_log=True)
sub_client.req_candlestick("btcusdt", CandlestickInterval.DAY1, callback)

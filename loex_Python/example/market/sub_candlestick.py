
from loex.client.market import MarketClient
from loex.constant import *
from loex.exception.loex_api_exception import LoexApiException


def callback(candlestick_event):
    print(candlestick_event)


def error(e: 'LoexApiException'):
    print(e.error_code + e.error_message)

market_client = MarketClient()
market_client.sub_candlestick("btcusdt", CandlestickInterval.DAY1, callback, error)


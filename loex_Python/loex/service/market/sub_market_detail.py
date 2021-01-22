import time

from loex.utils import *

from loex.connection.subscribe_client import SubscribeClient
from loex.model.market import *



class SubMarketDetailService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol = self.params["symbol"]

        def subscription(connection):
            if(symbol != ""):
                connection.send(market_detail_channel(symbol))
            else:
                connection.send(market_all_detail_channel())

        SubscribeClient(**kwargs).execute_subscribe_v1(subscription,
                                            None,
                                            callback,
                                            error_handler)




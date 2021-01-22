import time

from loex.utils import *

from loex.connection.subscribe_client import SubscribeClient
from loex.model.market import *



class SubCandleStickService:
    def __init__(self, params):

        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol = self.params["symbol"]
        interval = self.params["interval"]

        def subscription(connection):
            connection.send(kline_channel(symbol, interval))

        SubscribeClient(**kwargs).execute_subscribe_v1(subscription,
                                            None,
                                            callback,
                                            error_handler)




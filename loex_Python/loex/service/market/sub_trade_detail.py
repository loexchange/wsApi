import time

from loex.model.market import *
from loex.utils import *
from loex.connection.subscribe_client import SubscribeClient


class SubTradeDetailService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol = self.params["symbol"]

        def subscription(connection):
            connection.send(trade_detail_channel(symbol))

        SubscribeClient(**kwargs).execute_subscribe_v1(subscription,
                                            None,
                                            callback,
                                            error_handler)




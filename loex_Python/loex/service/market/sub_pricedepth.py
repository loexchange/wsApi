import time

from loex.model.market import *
from loex.utils import *
from loex.connection.subscribe_client import SubscribeClient


class SubPriceDepthService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol = self.params["symbol"]
        step = self.params["step"]
        
        def subscription(connection):
            connection.send(price_depth_channel(symbol, step))

        SubscribeClient(**kwargs).execute_subscribe_v2(subscription,
                                            None,
                                            callback,
                                            error_handler)




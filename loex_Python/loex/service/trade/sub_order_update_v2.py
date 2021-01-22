import time


from loex.connection.subscribe_client import SubscribeClient
from loex.model.trade import *
from loex.utils import *


class SubOrderUpdateV2Service:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol = self.params["symbol"]

        def subscription(connection):
            connection.send(orders_update_channel(symbol))

        SubscribeClient(**kwargs).execute_subscribe_v2(subscription,
                                            None,
                                            callback,
                                            error_handler,
                                            is_trade=True)








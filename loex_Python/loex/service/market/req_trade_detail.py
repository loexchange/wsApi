import time

from loex.model.market import *
from loex.utils import *
from loex.connection.websocket_req_client import *


class ReqTradeDetailService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol = self.params["symbol"]

        def subscription(connection):
            connection.send(request_trade_detail_channel(symbol))

        WebSocketReqClient(**kwargs).execute_subscribe_v1(subscription,
                                            None,
                                            callback,
                                            error_handler)




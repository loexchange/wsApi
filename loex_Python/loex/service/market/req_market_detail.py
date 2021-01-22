import time

from loex.utils import *

from loex.connection.websocket_req_client import *
from loex.model.market import *
from loex.utils.channels_request import *


class ReqMarketDetailService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol = self.params["symbol"]

        def subscription(connection):
             connection.send(request_market_detail_channel(symbol))

        WebSocketReqClient(**kwargs).execute_subscribe_v1(subscription,
                                            None,
                                            callback,
                                            error_handler)




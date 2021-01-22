import time

from loex.utils import *

from loex.connection.websocket_req_client import *
from loex.model.market import *
from loex.utils.channels_request import *


class ReqCandleStickService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        symbol = self.params["symbol"]
        interval = self.params["interval"]
        from_ts_second = self.params.get("from_ts_second", None)
        end_ts_second = self.params.get("end_ts_second", None)

        def subscription(connection):
            connection.send(request_kline_channel(symbol, interval, from_ts_second, end_ts_second))

        WebSocketReqClient(**kwargs).execute_subscribe_v1(subscription,
                                            None,
                                            callback,
                                            error_handler)




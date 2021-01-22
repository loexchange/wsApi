from loex.constant import *
from loex.model.trade import *
from loex.utils.input_checker import *


class TradeClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from loex.
            secret_key: The private key applied from loex.
            url: The URL name like "https://api.loex.pro".
            init_log: to init logger
        """
        self.__kwargs = kwargs

    def sub_order_update(self, symbol: 'str', callback, error_handler=None):
        """
        Subscribe order changing event. If a order is created, canceled etc, server will send the data to client and onReceive in callback will be called.

        :param symbol: The symbol, like "btcusdt".
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(order_update_event: 'OrderUpdateEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Loex server
            example: def error_handler(exception: 'LoexApiException')
                        pass
        :return:  No return
        """
        check_symbol(symbol)
        check_should_not_none(callback, "callback")

        params = {
            "symbol" : symbol,
        }

        from loex.service.trade.sub_order_update_v2 import SubOrderUpdateV2Service
        SubOrderUpdateV2Service(params).subscribe(callback, error_handler, **self.__kwargs)


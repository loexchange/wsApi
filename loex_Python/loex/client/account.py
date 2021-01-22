from loex.constant import *
from loex.model.account import *
from loex.utils import *
import aiohttp
import asyncio
from loex.utils.input_checker import check_in_list


class AccountClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from loex.
            secret_key: The private key applied from loex.
            url: The URL name like "https://api.loex.pro".
            init_log: Init logger, default is False, True will init logger handler
        """
        self.__kwargs = kwargs

    def sub_account_update(self, callback, error_handler=None):
        """
        Subscribe accounts update

        :param mode: subscribe mode
                "0" : for balance
                "1" : for available and balance
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(price_depth_event: 'PriceDepthEvent'):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Loex server
            example: def error_handler(exception: 'LoexApiException')
                        pass

        :return:  No return
        """

        params = {}

        from loex.service.account.sub_account_update import SubAccountUpdateService
        SubAccountUpdateService(params).subscribe(callback, error_handler, **self.__kwargs)

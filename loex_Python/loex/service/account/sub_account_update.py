from loex.utils import *

from loex.connection.subscribe_client import SubscribeClient
from loex.model.account import *


class SubAccountUpdateService:
    def __init__(self, params):
        self.params = params

    def subscribe(self, callback, error_handler, **kwargs):
        def subscription(connection):
            connection.send(accounts_update_channel())

        SubscribeClient(**kwargs).execute_subscribe_v2(subscription,
                                                       None,
                                                       callback,
                                                       error_handler,
                                                       is_trade=True)

from loex.client.account import AccountClient
from loex.constant import *
from loex.utils import *


def callback(account_change_event):
    print(account_change_event)


account_client = AccountClient(api_key=g_api_key,
                              secret_key=g_secret_key,
                              init_log=True)
account_client.sub_account_update(callback)


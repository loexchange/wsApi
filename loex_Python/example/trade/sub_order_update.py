
from loex.client.trade import TradeClient
from loex.constant import *


def callback(upd_event):
    print(upd_event)


trade_client = TradeClient(api_key=g_api_key, secret_key=g_secret_key, init_log=True)
trade_client.sub_order_update("btcusdt", callback)

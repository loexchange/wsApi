import json
from loex.utils.time_service import get_current_timestamp
from loex.constant import DepthStep


def kline_channel(symbol, interval):
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "market_" + symbol + "_kline_" + interval
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def trade_detail_channel(symbol):
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "market_" + symbol + "_trade_ticker"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def price_depth_channel(symbol, step_type=DepthStep.STEP0):
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "market_" + symbol + "_depth_" + step_type
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def orders_update_channel(symbol):
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "orders_{symbol}".format(symbol=symbol)
    return json.dumps(channel)


def market_detail_channel(symbol):
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "market_" + symbol + "_ticker"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)

def market_all_detail_channel():
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "market_ticker"
    channel["id"] = str(get_current_timestamp())
    return json.dumps(channel)


def accounts_update_channel():
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "accounts_update"
    return json.dumps(channel)


def trade_clearing_channel(symbol="*"):
    channel = dict()
    channel["action"] = "sub"
    channel["ch"] = "trade.clearing#" + symbol
    return json.dumps(channel)

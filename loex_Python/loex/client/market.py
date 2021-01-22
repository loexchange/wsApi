from loex.constant import *
from loex.model.market import *
from loex.utils import *
from loex.utils.input_checker import check_in_list


class MarketClient(object):

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

    def sub_candlestick(self, symbol: 'str', interval: 'CandlestickInterval', callback, error_handler):

        """
        Subscribe candlestick/kline event. If the candlestick/kline is updated, server will send the data to client and onReceive in callback will be called.

        :param symbol: The symbol, like "btcusdt".
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc.
        :param callback: The implementation is required. onReceive will be called if receive server's update.
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Loex server
            example: def error_handler(exception: 'LoexApiException')
                        pass
        :return: No return
        """

        check_symbol(symbol)
        check_should_not_none(interval, "interval")
        check_should_not_none(callback, "callback")

        params = {
            "symbol": symbol,
            "interval": interval,
        }

        from loex.service.market.sub_candlestick import SubCandleStickService
        SubCandleStickService(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_candlestick(self, symbol: 'str', interval: 'CandlestickInterval', callback,
                        from_ts_second=None, end_ts_second=None, error_handler=None):
        """
        Subscribe candlestick/kline event. If the candlestick/kline is updated, server will send the data to client and onReceive in callback will be called.

        :param symbol: The symbol, like "btcusdt".
        :param interval: The candlestick/kline interval, MIN1, MIN5, DAY1 etc.
        :param callback: The implementation is required. onReceive will be called if receive server's update.
                        pass
        :param from_ts_second : data from timestamp [it's second]
        :param end_ts_second : data util timestamp [it's second]
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Loex server
            example: def error_handler(exception: 'LoexApiException')
                        pass
        :return: No return
        """

        check_symbol(symbol)
        check_should_not_none(interval, "interval")
        check_should_not_none(callback, "callback")

        params = {
            "symbol": symbol,
            "interval": interval,
            "from_ts_second": from_ts_second,
            "end_ts_second": end_ts_second
        }

        from loex.service.market.req_candlestick import ReqCandleStickService
        ReqCandleStickService(params).subscribe(callback, error_handler, **self.__kwargs)

   
    @staticmethod
    def get_depth_step_list():
        return [DepthStep.STEP0,
                DepthStep.STEP1,
                DepthStep.STEP2,
                DepthStep.STEP3,
                DepthStep.STEP4,
                DepthStep.STEP5]

    @staticmethod
    def get_valid_depth_step(value, defalut_value):
        step_list = MarketClient.get_depth_step_list()
        if value in step_list:
            return value
        else:
            return defalut_value

    def sub_pricedepth(self, symbol: 'str', depth_step: 'str', callback, error_handler=None):
        """
        Subscribe price depth event. If the price depth is updated, server will send the data to client and onReceive in callback will be called.

        :param symbol: The symbol, like "btcusdt"
        :param depth_step: The depth precision, string from step0 to step5.
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(price_depth_event):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Loex server
            example: def error_handler(exception: 'LoexApiException')
                        pass

        :return:  No return
        """
        
        check_symbol(symbol)
        new_step = MarketClient.get_valid_depth_step(value=depth_step, defalut_value=DepthStep.STEP0)
        check_should_not_none(callback, "callback")

        params = {
            "symbol": symbol,
            "step": new_step,
        }

        from loex.service.market.sub_pricedepth import SubPriceDepthService
        SubPriceDepthService(params).subscribe(callback, error_handler, **self.__kwargs)

    def sub_market_detail(self, symbol: 'str', callback, error_handler=None):
        """
        Subscribe 24 hours trade statistics event. If statistics is generated, server will send the data to client and onReceive in callback will be called.

        :param symbol: The symbol, like "btcusdt". 
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(trade_statistics_event):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Loex server
            example: def error_handler(exception: 'LoexApiException')
                        pass
        :return:  No return
        """
        check_symbol(symbol)
        check_should_not_none(callback, "callback")

        params = {
            "symbol": symbol,
        }

        from loex.service.market.sub_market_detail import SubMarketDetailService
        SubMarketDetailService(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_market_detail(self, symbol: 'str', callback, error_handler=None):
        """
        Subscribe 24 hours trade statistics event. If statistics is generated, server will send the data to client and onReceive in callback will be called.

        :param symbol: The symbol, like "btcusdt"
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(trade_statistics_event):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Loex server
            example: def error_handler(exception: 'LoexApiException')
                        pass
        :return:  No return
        """
        check_symbol(symbol)
        check_should_not_none(callback, "callback")

        params = {
            "symbol": symbol,
        }

        from loex.service.market.req_market_detail import ReqMarketDetailService
        ReqMarketDetailService(params).subscribe(callback, error_handler, **self.__kwargs)

    def sub_trade_detail(self, symbol: 'str', callback, error_handler=None):
        """
        Subscribe price depth event. If the price depth is updated, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(trade_event):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Loex server
            example: def error_handler(exception: 'LoexApiException')
                        pass
        :return:  No return
        """
        check_symbol(symbol)
        check_should_not_none(callback, "callback")

        params = {
            "symbol": symbol,
        }

        from loex.service.market.sub_trade_detail import SubTradeDetailService
        SubTradeDetailService(params).subscribe(callback, error_handler, **self.__kwargs)

    def req_trade_detail(self, symbol: 'str', callback, error_handler=None):
        """
        Subscribe price depth event. If the price depth is updated, server will send the data to client and onReceive in callback will be called.

        :param symbols: The symbols, like "btcusdt". Use comma to separate multi symbols, like "btcusdt,ethusdt".
        :param callback: The implementation is required. onReceive will be called if receive server's update.
            example: def callback(trade_event):
                        pass
        :param error_handler: The error handler will be called if subscription failed or error happen between client and Loex server
            example: def error_handler(exception: 'LoexApiException')
                        pass
        :return:  No return
        """
        check_symbol(symbol)
        check_should_not_none(callback, "callback")

        params = {
            "symbol": symbol,
        }

        from loex.service.market.req_trade_detail import ReqTradeDetailService
        ReqTradeDetailService(params).subscribe(callback, error_handler, **self.__kwargs)

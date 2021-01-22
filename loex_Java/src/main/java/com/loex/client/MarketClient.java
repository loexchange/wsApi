package com.loex.client;

import com.alibaba.fastjson.JSONObject;
import com.loex.client.req.market.*;
import com.loex.constant.Options;
import com.loex.constant.enums.ExchangeEnum;
import com.loex.exception.SDKException;
import com.loex.service.LoexMarketService;
import com.loex.utils.ResponseCallback;

public interface MarketClient {

  void subCandlestick(SubCandlestickRequest request, ResponseCallback<JSONObject> callback);

  void subMarketDetail(SubMarketDetailRequest request, ResponseCallback<JSONObject> callback);

  void subMarketAllDetail(ResponseCallback<JSONObject> callback);

  void subMarketDepth(SubMarketDepthRequest request, ResponseCallback<JSONObject> callback);

  void subMarketTrade(SubMarketTradeRequest request, ResponseCallback<JSONObject> callback);

  void reqCandlestick(ReqCandlestickRequest request, ResponseCallback<JSONObject> callback);

  void reqMarketDepth(ReqMarketDepthRequest request, ResponseCallback<JSONObject> callback);

  void reqMarketTrade(ReqMarketTradeRequest request, ResponseCallback<JSONObject> callback);

  void reqMarketDetail(ReqMarketDetailRequest request, ResponseCallback<JSONObject> callback);

  static MarketClient create(Options options) {

    if (options.getExchange().equals(ExchangeEnum.LOEX)) {
      return new LoexMarketService(options);
    }
    throw new SDKException(SDKException.INPUT_ERROR, "Unsupport Exchange.");
  }


}

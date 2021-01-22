package com.loex.client;

import com.alibaba.fastjson.JSONObject;
import com.loex.client.req.trade.SubOrderUpdateRequest;
import com.loex.constant.Options;
import com.loex.constant.enums.ExchangeEnum;
import com.loex.exception.SDKException;
import com.loex.service.LoexTradeService;
import com.loex.utils.ResponseCallback;

public interface TradeClient {


  void subOrderUpdateV2(SubOrderUpdateRequest request, ResponseCallback<JSONObject> callback);

  static TradeClient create(Options options) {

    if (options.getExchange().equals(ExchangeEnum.LOEX)) {
      return new LoexTradeService(options);
    }
    throw new SDKException(SDKException.INPUT_ERROR, "Unsupport Exchange.");
  }

}

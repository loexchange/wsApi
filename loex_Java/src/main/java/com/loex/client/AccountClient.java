package com.loex.client;

import com.alibaba.fastjson.JSONObject;
import com.loex.constant.Options;
import com.loex.constant.enums.ExchangeEnum;
import com.loex.exception.SDKException;
import com.loex.service.LoexAccountService;
import com.loex.utils.ResponseCallback;

public interface AccountClient {

  void subAccountsUpdate(ResponseCallback<JSONObject> callback);

  static AccountClient create(Options options) {

    if (options.getExchange().equals(ExchangeEnum.LOEX)) {
      return new LoexAccountService(options);
    }
    throw new SDKException(SDKException.INPUT_ERROR, "Unsupport Exchange.");
  }
}

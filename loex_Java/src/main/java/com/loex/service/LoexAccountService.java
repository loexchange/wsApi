package com.loex.service;

import com.alibaba.fastjson.JSONObject;
import com.loex.client.AccountClient;
import com.loex.constant.Options;
import com.loex.constant.WebSocketConstants;
import com.loex.service.connection.LoexWebSocketConnection;
import com.loex.utils.ResponseCallback;

import java.util.ArrayList;
import java.util.List;

public class LoexAccountService implements AccountClient {

  public static final String SUB_ACCOUNT_UPDATE_TOPIC = "accounts_update";

  private Options options;

  public LoexAccountService(Options options) {
    this.options = options;
  }

  @Override
  public void subAccountsUpdate(ResponseCallback<JSONObject> callback) {
    JSONObject command = new JSONObject();
    command.put("action", WebSocketConstants.ACTION_SUB);
    command.put("cid", System.currentTimeMillis() + "");
    command.put("ch", SUB_ACCOUNT_UPDATE_TOPIC);

    List<String> commandList = new ArrayList<>();
    commandList.add(command.toJSONString());

    LoexWebSocketConnection.createAssetConnection(options, commandList, null, callback, false);
  }

}

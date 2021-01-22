package com.loex.service;

import com.alibaba.fastjson.JSONObject;
import com.loex.client.TradeClient;
import com.loex.client.req.trade.SubOrderUpdateRequest;
import com.loex.constant.Options;
import com.loex.constant.WebSocketConstants;
import com.loex.service.connection.LoexWebSocketConnection;
import com.loex.utils.InputChecker;
import com.loex.utils.ResponseCallback;

import java.util.ArrayList;
import java.util.List;

public class LoexTradeService implements TradeClient {

  public static final String WEBSOCKET_ORDER_UPDATE_V2_TOPIC = "orders_${symbol}";


  private Options options;


  private LoexAccountService loexAccountService;

  public LoexTradeService(Options options) {
    this.options = options;
    this.loexAccountService = new LoexAccountService(options);
  }

  @Override
  public void subOrderUpdateV2(SubOrderUpdateRequest request, ResponseCallback<JSONObject> callback) {
    // 检查参数
    InputChecker.checker()
        .shouldNotNull(request.getSymbol(), "symbols");


    // 检查数组
    InputChecker.checker().checkSymbol(request.getSymbol());

    List<String> commandList = new ArrayList<>(1);
    String topic = WEBSOCKET_ORDER_UPDATE_V2_TOPIC
            .replace("${symbol}", request.getSymbol());

    JSONObject command = new JSONObject();
    command.put("action", WebSocketConstants.ACTION_SUB);
    command.put("ch", topic);
    command.put("id", System.nanoTime());
    commandList.add(command.toJSONString());

    LoexWebSocketConnection.createAssetConnection(options, commandList, null, callback, false);
  }

}

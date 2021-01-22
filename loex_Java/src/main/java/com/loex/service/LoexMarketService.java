package com.loex.service;

import com.alibaba.fastjson.JSONObject;
import com.loex.client.MarketClient;
import com.loex.client.req.market.*;
import com.loex.constant.Options;
import com.loex.constant.WebSocketConstants;
import com.loex.constant.enums.DepthStepEnum;
import com.loex.service.connection.LoexWebSocketConnection;
import com.loex.utils.InputChecker;
import com.loex.utils.ResponseCallback;
import com.loex.utils.SymbolUtils;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class LoexMarketService implements MarketClient {

  private Options options;

  public LoexMarketService(Options options) {
    this.options = options;
  }


  public static final String WEBSOCKET_CANDLESTICK_TOPIC = "market_$symbol$_kline_$period$";
  public static final String WEBSOCKET_MARKET_DETAIL_TOPIC = "market_$symbol_ticker";
  public static final String WEBSOCKET_MARKET_DETAIL_ALL_TOPIC = "market_ticker";
  public static final String WEBSOCKET_MARKET_DEPTH_TOPIC = "market_$symbol_depth_$type";
  public static final String WEBSOCKET_MARKET_TRADE_TOPIC = "market_$symbol_trade_ticker";


  @Override
  public void subCandlestick(SubCandlestickRequest request, ResponseCallback<JSONObject> callback) {

    // 检查参数
    InputChecker.checker()
        .shouldNotNull(request.getSymbol(), "symbol")
        .shouldNotNull(request.getInterval(), "interval");
    // 格式化symbol为数组
    List<String> symbolList = SymbolUtils.parseSymbols(request.getSymbol());

    // 检查数组
    InputChecker.checker()
        .checkSymbolList(symbolList);

    List<String> commandList = new ArrayList<>(symbolList.size());
    symbolList.forEach(symbol -> {

      String topic = WEBSOCKET_CANDLESTICK_TOPIC
          .replace("$symbol$", symbol)
          .replace("$period$", request.getInterval().getCode());

      JSONObject command = new JSONObject();
      command.put("action", WebSocketConstants.ACTION_SUB);
      command.put("ch", topic);
      commandList.add(command.toJSONString());
    });

    LoexWebSocketConnection.createMarketConnection(options, commandList, null, callback, false);
  }

  @Override
  public void subMarketAllDetail(ResponseCallback<JSONObject> callback) {
    List<String> commandList = new ArrayList<>(1);
    String topic = WEBSOCKET_MARKET_DETAIL_ALL_TOPIC;

    JSONObject command = new JSONObject();
    command.put("action", WebSocketConstants.ACTION_SUB);
    command.put("ch", topic);
    commandList.add(command.toJSONString());

    LoexWebSocketConnection.createMarketConnection(options, commandList, null, callback, false);
  }

  @Override
  public void subMarketDetail(SubMarketDetailRequest request, ResponseCallback<JSONObject> callback) {
    // 检查参数
    InputChecker.checker()
        .shouldNotNull(request.getSymbol(), "symbol");

    List<String> commandList = new ArrayList<>(1);
    String topic = WEBSOCKET_MARKET_DETAIL_TOPIC
            .replace("$symbol", request.getSymbol());

    JSONObject command = new JSONObject();
    command.put("action", WebSocketConstants.ACTION_SUB);
    command.put("ch", topic);
    commandList.add(command.toJSONString());

    LoexWebSocketConnection.createMarketConnection(options, commandList, null, callback, false);
  }


  @Override
  public void subMarketDepth(SubMarketDepthRequest request, ResponseCallback<JSONObject> callback) {
    // 检查参数
    InputChecker.checker()
        .shouldNotNull(request.getSymbol(), "symbol");

    String step = request.getStep() == null ? DepthStepEnum.STEP0.getStep() : request.getStep().getStep();
    List<String> commandList = new ArrayList<>(1);
    String topic = WEBSOCKET_MARKET_DEPTH_TOPIC
            .replace("$symbol", request.getSymbol())
            .replace("$type", step);

    JSONObject command = new JSONObject();
    command.put("action", WebSocketConstants.ACTION_SUB);
    command.put("ch", topic);
    command.put("id", System.nanoTime());
    commandList.add(command.toJSONString());

    LoexWebSocketConnection.createMarketConnection(options, commandList, null, callback, false);
  }

  @Override
  public void subMarketTrade(SubMarketTradeRequest request, ResponseCallback<JSONObject> callback) {

    // 检查参数
    InputChecker.checker()
        .shouldNotNull(request.getSymbol(), "symbol");

    // 格式化symbol为数组
    List<String> symbolList = SymbolUtils.parseSymbols(request.getSymbol());

    // 检查数组
    InputChecker.checker()
        .checkSymbolList(symbolList);

    List<String> commandList = new ArrayList<>(symbolList.size());
    symbolList.forEach(symbol -> {

      String topic = WEBSOCKET_MARKET_TRADE_TOPIC
          .replace("$symbol", symbol);

      JSONObject command = new JSONObject();
      command.put("action", WebSocketConstants.ACTION_SUB);
      command.put("ch", topic);
      command.put("id", System.nanoTime());
      commandList.add(command.toJSONString());
    });

    LoexWebSocketConnection.createMarketConnection(options, commandList, null, callback, false);
  }


  @Override
  public void reqCandlestick(ReqCandlestickRequest request, ResponseCallback<JSONObject> callback) {

    // 检查参数
    InputChecker.checker()
        .shouldNotNull(request.getSymbol(), "symbol")
        .shouldNotNull(request.getInterval(), "interval");

    String topic = WEBSOCKET_CANDLESTICK_TOPIC
        .replace("$symbol$", request.getSymbol())
        .replace("$period$", request.getInterval().getCode());

    JSONObject command = new JSONObject();
    command.put("action", WebSocketConstants.OP_REQ);
    command.put("ch", topic);
    if (request.getFrom() != null) {
      command.put("from", request.getFrom());
    }
    if (request.getTo() != null) {
      command.put("to", request.getTo());
    }
    command.put("params", new HashMap<>());
    List<String> commandList = new ArrayList<>(1);
    commandList.add(command.toJSONString());

    LoexWebSocketConnection.createMarketConnection(options, commandList, null, callback, true);
  }

  @Override
  public void reqMarketDepth(ReqMarketDepthRequest request, ResponseCallback<JSONObject> callback) {
    // 检查参数
    InputChecker.checker()
        .shouldNotNull(request.getSymbol(), "symbol")
        .shouldNotNull(request.getStep(), "step");

    String topic = WEBSOCKET_MARKET_DEPTH_TOPIC
        .replace("$symbol", request.getSymbol())
        .replace("$type", request.getStep().getStep());

    JSONObject command = new JSONObject();
    command.put("action", WebSocketConstants.OP_REQ);
    command.put("ch", topic);

    List<String> commandList = new ArrayList<>(1);
    commandList.add(command.toJSONString());
    LoexWebSocketConnection.createMarketConnection(options, commandList, null, callback, true);

  }

  @Override
  public void reqMarketTrade(ReqMarketTradeRequest request, ResponseCallback<JSONObject> callback) {
    // 检查参数
    InputChecker.checker()
        .shouldNotNull(request.getSymbol(), "symbol");

    String topic = WEBSOCKET_MARKET_TRADE_TOPIC
        .replace("$symbol", request.getSymbol());

    JSONObject command = new JSONObject();
    command.put("action", WebSocketConstants.OP_REQ);
    command.put("ch", topic);

    List<String> commandList = new ArrayList<>(1);
    commandList.add(command.toJSONString());
    LoexWebSocketConnection.createMarketConnection(options, commandList, null, callback, true);
  }

  @Override
  public void reqMarketDetail(ReqMarketDetailRequest request, ResponseCallback<JSONObject> callback) {
    // 检查参数
    InputChecker.checker()
        .shouldNotNull(request.getSymbol(), "symbol");

    String topic = WEBSOCKET_MARKET_DETAIL_TOPIC
        .replace("$symbol", request.getSymbol());

    JSONObject command = new JSONObject();
    command.put("action", WebSocketConstants.OP_REQ);
    command.put("ch", topic);

    List<String> commandList = new ArrayList<>(1);
    commandList.add(command.toJSONString());
    LoexWebSocketConnection.createMarketConnection(options, commandList, null, callback, true);
  }


}

package com.loex.examples;

import com.loex.client.MarketClient;
import com.loex.client.req.market.*;
import com.loex.constant.LoexOptions;
import com.loex.constant.enums.CandlestickIntervalEnum;

public class MarketClientExample {

  public static void main(String[] args) {

    MarketClient marketClient = MarketClient.create(new LoexOptions());

    String symbol = "btcusdt";

    //请求K线数据
    marketClient.reqCandlestick(ReqCandlestickRequest.builder()
            .symbol(symbol)
            .interval(CandlestickIntervalEnum.DAY1)
            .build(), candlestickReq -> {

      System.out.println("candlestick:" + candlestickReq.toString());
    });
    //订阅K线数据
    marketClient.subCandlestick(SubCandlestickRequest.builder()
        .symbol(symbol)
        .interval(CandlestickIntervalEnum.DAY1)
        .build(), (candlestick) -> {

      System.out.println(candlestick.toString());
    });

    //订阅24小时市场行情
   marketClient.subMarketDetail(SubMarketDetailRequest.builder().symbol(symbol).build(), (marketDetailEvent) -> {
      System.out.println(marketDetailEvent.toString());
    });

    marketClient.subMarketAllDetail((marketDetailEvent) -> {
      System.out.println(marketDetailEvent.toString());
    });


    //订阅市场深度行情数据
    marketClient.subMarketDepth(SubMarketDepthRequest.builder().symbol(symbol).build(), (marketDetailEvent) -> {
      System.out.println(marketDetailEvent.toString());
    });

    //订阅实时成交数据
    marketClient.subMarketTrade(SubMarketTradeRequest.builder().symbol(symbol).build(), (marketTradeEvent) -> {
      System.out.println(marketTradeEvent.toString());
    });

    //请求实时成交数据
    marketClient.reqMarketTrade(ReqMarketTradeRequest.builder()
            .symbol(symbol)
            .build(), marketTradeReq -> {

      System.out.println(marketTradeReq.toString());
    });

  }


}

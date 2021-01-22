package com.loex.examples;

import com.loex.Constants;
import com.loex.client.TradeClient;
import com.loex.client.req.trade.SubOrderUpdateRequest;
import com.loex.constant.LoexOptions;

public class TradeClientExample {

  public static void main(String[] args) {

    TradeClient tradeService = TradeClient.create(LoexOptions.builder()
        .apiKey(Constants.API_KEY)
        .secretKey(Constants.SECRET_KEY)
        .build());


    tradeService.subOrderUpdateV2(SubOrderUpdateRequest.builder().symbol("btcusdt").build(), orderUpdateV2Event -> {

      System.out.println(orderUpdateV2Event.toString());

    });

  }

}

package com.loex.examples;

import com.loex.Constants;
import com.loex.client.AccountClient;
import com.loex.constant.LoexOptions;

public class AccountClientExample {

  public static void main(String[] args) {

    AccountClient accountService = AccountClient.create(LoexOptions.builder()
            .apiKey(Constants.API_KEY)
            .secretKey(Constants.SECRET_KEY)
            .build());


    accountService.subAccountsUpdate( event -> {
      System.out.println(event.toString());
    });

  }

}

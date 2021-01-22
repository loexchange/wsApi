package com.loex.constant;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.NoArgsConstructor;
import lombok.ToString;

import com.loex.constant.enums.ExchangeEnum;

@Builder
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class LoexOptions implements Options {

  @Builder.Default
  private String restHost = "https://xxxxxxx.io";

  @Builder.Default
  private String websocketHost = "ws://xxxxxx/ws";

  private String apiKey;

  private String secretKey;

  @Builder.Default
  private boolean websocketAutoConnect = true;

  @Override
  public String getApiKey() {
    return this.apiKey;
  }

  @Override
  public String getSecretKey() {
    return this.secretKey;
  }

  @Override
  public ExchangeEnum getExchange() {
    return ExchangeEnum.LOEX;
  }

  @Override
  public String getRestHost() {
    return this.restHost;
  }

  @Override
  public String getWebSocketHost() {
    return this.websocketHost;
  }

  @Override
  public boolean isWebSocketAutoConnect() {
    return this.websocketAutoConnect;
  }

}

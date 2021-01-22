package com.loex.constant.enums;

import lombok.Getter;

@Getter
public enum ExchangeEnum {

  HUOBI("huobi"),
  LOEX("loex"),
  ;
  private final String code;
  ExchangeEnum(String code) {
    this.code = code;
  }

}

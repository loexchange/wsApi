package com.loex.constant.enums;

import lombok.AllArgsConstructor;
import lombok.Getter;

/**
 *  The aggregation depth type.
 */
@Getter
@AllArgsConstructor
public enum DepthStepEnum {

  /**
   * step0,step1,step2
   */
  STEP0("step0"),
  STEP1("step1"),
  STEP2("step2")
  ;

  private final String step;

}

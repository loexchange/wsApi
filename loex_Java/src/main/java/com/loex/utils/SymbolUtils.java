package com.loex.utils;

import java.util.Arrays;
import java.util.List;

public class SymbolUtils {

  public static List<String> parseSymbols(String symbol) {
    return Arrays.asList(symbol.split("[,]"));
  }

}

package com.loex.service.parser;

import java.util.List;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

public interface LoexModelParser<T> {


  T parse(JSONObject json);

  T parse(JSONArray json);

  List<T> parseArray(JSONArray jsonArray);

}

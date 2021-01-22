# 订阅K线数据

- 订阅主题

```
market_$symbol_kline_$period
```

- 说明

  一旦K线数据产生，Websocket服务器将通过此订阅主题接口推送至客户端

- 订阅参数

  | 参数 | 数据类型 | 描述 |
  | --- | --- | --- |
  | symbol | string | 交易币对 |
  | period | string | K线周期(1min, 5min, 15min, 30min, 60min, 4h, 1day, 1mon, 1week) |

- 返回信息

  | 字段名 | 数据类型 | 描述 |
  | --- | --- | --- |
  | idx | long |unix时间，同时作为K线ID |
  | amount | BigDecimal | 成交额，即 sum(每一笔成交价 * 该笔的成交量) |
  | open | BigDecimal | 开盘价 |
  | close | BigDecimal | 收盘价（当K线为最晚的一根时，是最新成交价） |
  | low | BigDecimal | 最低价 |
  | high | BigDecimal | 最高价|
  | vol | BigDecimal | 成交量 |

- 示例

###### Subscribe Request

```
{
  "action": "sub",
  "ch": "market_btcusdt_kline_1day"
}
```

###### Subscribe Response

```
{
    "action": "sub",
    "code": 200,
    "ch": "market_btcusdt_kline_1day",
    "data": {}
}
```

###### Update example

```
{
    "code": 200,
    "data": {
        "amount": 0.06100000,
        "vol": 0.00610000,
        "high": 10.00000000,
        "low": 10.00000000,
        "_id": "1611072000",
        "idx": 1611072000,
        "close": 10.00000000,
        "open": 10.00000000
    },
    "ch": "market_btcusdt_kline_1day",
    "action": "push",
    "ts": 1611114854606
}
```

- 请求参数

  | 参数 | 数据类型 | 描述 |
  | --- | --- | --- |
  | from | integer | 起始时间 |
  | to | integer | 结束时间 |

###### Request

```
{
  "action": "req",
  "ch": "market_btcusdt_kline_1min",
  "params":{
    "from": "from time in epoch seconds",
    "to": "to time in epoch seconds"
  }
}
```

###### Response

```
{
    "code": 200,
    "data": [
      {
        "amount": 0.06100000,
        "vol": 0.00610000,
        "high": 10.00000000,
        "low": 10.00000000,
        "_id": "1611072000",
        "idx": 1611072000,
        "close": 10.00000000,
        "open": 10.00000000
      },
      {
        "amount": 0.06100000,
        "vol": 0.00610000,
        "high": 10.00000000,
        "low": 10.00000000,
        "_id": "1611072000",
        "idx": 1611072000,
        "close": 10.00000000,
        "open": 10.00000000
      },
      ...
    ],
    "ch": "market_btcusdt_kline_1min",
    "action": "req",
    "ts": 1611114854606
}
```
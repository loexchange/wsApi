# 订阅成交明细

- 订阅主题

```
market_$symbol_trade_ticker
```

- 说明

  此主题提供市场最新成交逐笔明细。

- 订阅参数

  | 参数 | 数据类型 | 描述 |
  | --- | --- | --- |
  | symbol | string | 交易币对 |


- 返回信息

  | 字段名 | 数据类型 | 描述 |
  | --- | --- | --- |
  | side | string |成交主动方 |
  | vol | BigDecimal |成交量（买或卖一方） |
  | amount | BigDecimal | 成交额 |
  | price | BigDecimal | 成交价格|
  | ts | long | 成交时间|
  | id | long | 成交id|
  | ds | string | 成交时间格式字符串|

- 示例

###### Subscribe Request

```
{
  "action": "sub",
  "ch": "market_btcusdt_trade_ticker"
}
```

###### Subscribe Response

```
{
    "action": "sub",
    "code": 200,
    "ch": "market_btcusdt_trade_ticker",
    "data": {}
}
```

###### Update example

```
{
    "action": "push",
    "ch": "market_btcusdt_trade_ticker",
    "code": 200,
    "data": [{
        "side": "SELL",
        "vol": 0.00010000,
        "amount": 0.00100000,
        "price": 10.00000000,
        "id": 97,
        "ts": 1611115579354,
        "ds": "2021-01-20 12:06:19"
    }],
    "ts": 1611115579434
}
```

- 请求

###### Request

```
{
  "action": "req",
  "ch": "market_btcusdt_trade_ticker"
}
```

###### Response

```
{
    "action": "req",
    "ch": "market_btcusdt_trade_ticker",
    "code": 200,
    "data": [{
        "side": "SELL",
        "vol": 0.001,
        "amount": 0.01,
        "price": 10.0,
        "id": 94,
        "ts": 1611115324643,
        "ds": "2021-01-20 12:02:04"
    }, {
        "side": "SELL",
        "vol": 1.0E-4,
        "amount": 0.001,
        "price": 10.0,
        "id": 93,
        "ts": 1611113838320,
        "ds": "2021-01-20 11:37:18"
    }
    ...
    , {
        "side": "SELL",
        "vol": 0.0063,
        "price": 9990.08,
        "id": 70102,
        "ts": 1564806700000,
        "ds": "2019-08-03 12:31:40"
    }],
    "ts": 1611115385790
}
```
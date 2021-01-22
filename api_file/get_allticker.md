# 订阅所有市场概要

- 订阅主题

```
market_ticker
```

- 说明

  此主题提供24小时内所有市场市场最新概要。

- 订阅参数

  | 参数 | 数据类型 | 描述 |
  | --- | --- | --- |
  | symbol | string | 交易币对 |

- 返回信息

  | 字段名 | 数据类型 | 描述 |
  | --- | --- | --- |
  | id | long |unix时间，同时作为消息ID |
  | amount | BigDecimal | 24小时成交额 |
  | open | BigDecimal | 24小时开盘价|
  | close | BigDecimal | 最新价 |
  | low | BigDecimal | 24小时最低价 |
  | high | BigDecimal | 24小时最高价|
  | vol | BigDecimal | 24小时成交量 |
  | rose | BigDecimal | 24小时涨跌幅 |
  | time | long | 时间戳 |

- 示例

###### Subscribe Request

```
{
  "action": "sub",
  "ch": "market_ticker"
}
```

###### Subscribe Response

```
{
    "action": "sub",
    "code": 200,
    "ch": "market_ticker",
    "data": {}
}
```

###### Update example

```
{
    "action": "push",
    "ch": "market_btcusdt_ticker",
    "code": 200,
    "data": {
        "amount": 10.20300000,
        "convertAmount": 64.12100000,
        "vol": 1.13030000,
        "high": 38448.00000000,
        "low": 9.00000000,
        "rose": 0E-8,
        "id": 1611115264,
        "time": 1611115381764,
        "close": 10.00000000,
        "open": 10.00000000
    },
    "ts": 1611115406118
}
```

###### Update example

```
{
    "action": "push",
    "ch": "market_ethusdt_ticker",
    "code": 200,
    "data": {
        "amount": 10.20300000,
        "convertAmount": 64.12100000,
        "vol": 1.13030000,
        "high": 38448.00000000,
        "low": 9.00000000,
        "rose": 0E-8,
        "id": 1611115264,
        "time": 1611115381764,
        "close": 10.00000000,
        "open": 10.00000000
    },
    "ts": 1611115406118
}
```
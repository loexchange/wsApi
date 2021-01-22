# 订阅市场深度行情数据

- 订阅主题

```
market_$symbol_depth_$type
```

- 说明

  此主题发送最新市场深度数据。

- 订阅参数

  | 参数 | 数据类型 | 描述 |
  | --- | --- | --- | 
  | symbol | string | 交易币对 |
  | type | string | 合并深度类型(step0, step1, step2) |


- 返回信息

  | 字段名 | 数据类型 | 描述 |
  | --- | --- | --- |
  | buys | object |当前的所有买单 [price, size] |
  | asks | object |当前的所有卖单 [price, size] |
  | ts | integer | 当前时间戳，单位毫秒|

- 示例

###### Subscribe Request

```
{
  "action": "sub",
  "ch": "market_ethusdt_depth_step0"
}
```

###### Subscribe Response

```
{
    "action": "sub",
    "code": 200,
    "ch": "market_ethusdt_depth_step0",
    "data": {}
}
```

###### Update example

```
{
    "action": "push",
    "ch": "market_ethusdt_depth_step0",
    "ts": 1611115406118,
    "code": 200,
    "data": {
        "buys": [
            [280.00, 2.0000],
            [260.00, 1.0000],
            [250.00, 1.0000],
            [200.00, 1.0000],
            [28.66, 3.0000],
            [3.00, 92.0000],
            [2.96, 1.0000]
        ],
        "asks": [
            [300.00, 0.5000]
        ]
    }
```

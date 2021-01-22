# 订阅订单更新
- 订阅主题
```
orders_$symbol
```

- 说明
    订单的更新推送由任一以下事件触发：（订阅前需先进行  [鉴权](auth.md) ）

    1、订单创建（eventType=creation）

    2、订单成交（eventType=trade）

    3、订单撤销（eventType=cancellation）

    不同事件类型所推送的消息中，字段列表略有不同。开发者可以采取以下两种方式设计返回的数据结构：
    定义一个包含所有字段的数据结构，并允许某些字段为空
    定义不同的数据结构，分别包含各自的字段，并继承自一个包含公共数据字段的数据结构
  
   
- 订阅参数
  
    | 参数 | 数据类型 | 描述 |
    | --- | --- | --- |
    | symbol | string | 交易币对 |
    

- 返回信息

1. 当订单挂单后
   
    | 字段名 | 数据类型 | 描述 |
    | --- | --- | --- |
    | eventType | string |事件类型，有效值：creation |
    | symbol | string | 交易币对 |
    | uid | integer | 用户id |
    | orderId | string | 订单号 |
    | orderSource | string | 订单来源，有效值：WEB,APP,API,H5,API-INNER |
    | orderPrice | string | 订单价格 |
    | orderSize | string | 订单数量 |
    | orderSide | string | 订单方向，有效值：BUY,SELL |
    | orderStatus | string | 订单状态，有效值：0 初始订单，1 新订单，2 完全成交，3 部分成交，4 已撤单，5 待撤单，6 异常订单 |
    | orderCreateTime | long | 订单创建时间 |
    | orderType | string | 委托类型 1:限价委托 2:市价委托 |
2. 当订单成交后
   
    | 字段名 | 数据类型 | 描述 |
    | --- | --- | --- |
    | eventType | string |事件类型，有效值：trade |
    | symbol | string | 交易币对 |
    | uid | integer | 用户id |
    | orderId | string | 订单号 |
    | tradeId | string | 成交订单id |
    | tradePrice | string | 成交价 |
    | tradeVolume | string | 成交量 |
    | aggressor | boolean | 是否交易主动方，有效值： true, false |
    | tradeTime | long | 成交时间 |
    | feeCurrency | string | 手续费币种 |
    | orderSource | string | 订单来源，有效值：WEB,APP,API,H5,API-INNER |
    | orderPrice | string | 订单价格 |
    | orderSize | string | 订单数量 |
    | orderSide | string | 订单方向，有效值：BUY,SELL |
    | orderStatus | string | 订单状态，有效值：0 初始订单，1 新订单，2 完全成交，3 部分成交，4 已撤单，5 待撤单，6 异常订单 |
    | orderCreateTime | long | 订单创建时间 |
    | orderType | string | 委托类型 1:限价委托 2:市价委托 |
3. 当订单被撤销后
   
    | 字段名 | 数据类型 | 描述 |
    | --- | --- | --- |
    | eventType | string |事件类型，有效值：cancellation |
    | symbol | string | 交易币对 |
    | uid | integer | 用户id |
    | orderId | string | 订单号 |
    | orderSource | string | 订单来源，有效值：WEB,APP,API,H5,API-INNER |
    | orderPrice | string | 订单价格 |
    | orderSize | string | 订单数量 |
    | remainAmt | string | 剩余数量 |
    | execAmt | string | 累计成交量 |
    | orderSide | string | 订单方向，有效值：BUY,SELL |
    | orderStatus | string | 订单状态，有效值：0 初始订单，1 新订单，2 完全成交，3 部分成交，4 已撤单，5 待撤单，6 异常订单 |
    | lastActTime | long | 订单更新时间 |
    | orderType | string | 委托类型 1:限价委托 2:市价委托 |

- 示例

###### Subscribe Request
```
{
    "action": "sub",
    "ch": "orders_btcusdt"
}
```
###### Subscribe Response
```
{
    "action": "sub",
    "code": 200,
    "ch": "orders_btcusdt",
    "data": {}
}
```
###### Update example (creation)
```
{
    "code": 200,
    "data": {
        "symbol": "btcusdt",
        "uid": 10046,
        "orderType": "1",
        "orderSource": "WEB",
        "orderId": 355,
        "orderCreateTime": 1611113789000,
        "orderSize": "0.001",
        "orderStatus": "0",
        "orderPrice": "10",
        "eventType": "creation",
        "orderSide": "SELL"
    },
    "ch": "orders_btcusdt",
    "action": "push"
}
```
###### Update example (trade)
```
{
    "code": 200,
    "data": {
        "tradeVolume": "0.0001",
        "symbol": "BTCUSDT",
        "orderType": "1",
        "aggressor": true,
        "orderId": 356,
        "orderSize": "0.0001",
        "feeCurrency": "BTC",
        "eventType": "trade",
        "orderSource": "WEB",
        "orderSide": "SELL",
        "tradeTime": 1611113838320,
        "uid": 10046,
        "oderStatus": "2",
        "orderPrice": "10",
        "tradePrice": "10",
        "tradeId": 93
    },
    "ch": "orders_btcusdt",
    "action": "push"
}
```
###### Update example (cancellation)
```
{
    "code": 200,
    "data": {
        "symbol": "btcusdt",
        "orderType": "1",
        "orderSource": "WEB",
        "remainAmt": "1",
        "orderId": 357,
        "orderSize": "1",
        "orderStatus": "4",
        "eventType": "cancellation",
        "orderSide": "BUY",
        "orderUpdateTime": 1611113854709,
        "execAmt": "0",
        "uid": 10046,
        "orderPrice": "11"
    },
    "ch": "orders_btcusdt",
    "action": "push"
}
```

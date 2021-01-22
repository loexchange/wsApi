# 订阅账户变更
- openAPI Key 权限：读取
- 订阅主题
```
accounts_update
```

- 说明
  
  在账户余额发生变动时推送。（订阅前需先进行  [鉴权](auth.md) ）

- 订阅参数 
  
  无

- 返回信息

    | 字段名 | 数据类型 | 描述 |
    | --- | --- | --- |
    | code | integer |编码 200=成功|
    | coin | string | 币种 |
    | account | long | 账户信息 |
    | balance | String | 账户余额|
    | changeType | string | 余额变动类型，有效值：order-create(订单创建)，order-match(订单成交)，order-refund(订单成交退款)，order-cancel(订单撤销)，deposit (充币）, withdraw (提币)，other(其他资产变化) |
    | accountType | string | 账户类型，有效值：normal, frozen |
    | changeTime | long | 余额变动时间，unix time in millisecond |

- 示例
###### Subscribe Request
```
{
    "action": "sub",
    "ch": "accounts_update"
}
```
###### Subscribe Response
```
{
    "action": "sub",
    "code": 200,
    "ch": "accounts_update",
    "data": {}
}
```
###### Update example
```
accounts_update：
{
    "action": "push",
    "ch": "accounts_update",
    "code": 200,
    "data": {
        "coin": "ETH",
        "account": 2011001,
        "balance": "8207.064772",
        "changeType": "order-create",
        "accountType": "normal",
        "changeTime": 1611109421362
    }
}
```

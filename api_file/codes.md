# 错误码

- 常见错误码

以下是openapi-ws接口的错误码、错误消息和说明。

| 错误码 | 错误消息 | 说明 |
| --- | --- | --- |
|200 |正确   | 正确返回  |
|404 |Not Found   | 找不到服务  |
|500 |系统异常   | 系统异常   |
|2001 |invalid.json   | 无效json字符串 |
|2001 |invalid.action   | 无效action指令   |
|2001 |invalid.ch   | 无效的ch通道   |
|2001 |auth.fail   | 授权失败   |
|2001 |invalid.auth.state   | 未授权   |
|2001 |invalid.symbol  | 无效币对   |
|2001 |invalid.operate   | 无效的操作   |
|2001 |missing.params   | 缺少params字段 |
|2001 |missing.params.apiKey   | 缺少params.apiKey字段  |
|2001 |missing.params.signature   | 缺少params.signature字段  |
|2001 |missing.params.signatureVersion   | 缺少params.signatureVersion字段   |
|2001 |missing.params.signatureMethod   | 缺少params.signatureMethod字段   |
|2001 |missing.params.timestamp   | 缺少params.timestamp字段   |
|2001 |invalid.sign.fail   | 签名错误   |

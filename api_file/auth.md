# 鉴权

- 请求主题

```
auth
```

- 说明

- 鉴权请求参数

  | 参数 | 数据类型 | 描述 |
  | --- | --- | --- |
  | apiKey | string | 您申请的apiKey |
  | signatureMethod | string | 签名方法，用户计算签名寄语哈希的协议，固定值为HmacSHA256 |
  | signatureVersion | string | 签名协议版本，固定值为1.0 |
  | timestamp | long | 时间戳，您发出请求的时间（UTC时间）在查询请求中包含此值有助于防止第三方截取您的请求。如：2017-05-11T16:22:06。再次强调是 (UTC 时区) |
  | signature | string | 签名, 计算得出的值，用于确保签名有效和未被篡改 |

- 鉴权成功后返回信息

  | 字段名 | 数据类型 | 描述 |
  | --- | --- | --- |
  | code | int |200:鉴权成功，其他:鉴权失败 [错误码](codes.md) |

- 签名步骤

1. 生成参与签名的固定参数名为：apiKey，signatureMethod，signatureVersion，timestamp
2. 对参数进行URL编码，并且按照ASCII码顺序进行排序
3. 将各参数使用字符 “&” 连接

```
   apiKey=0cxxxxxx-xxxxxx-xxxxxx-xxxx&signatureMethod=HmacSHA256&signatureVersion=1.0&timestamp=1611114854606
```

4. 用上一步里生成的 “请求字符串” 和你的密钥 (Secret Key) 生成一个数字签名

    1. 将上一步得到的请求字符串和 API 私钥作为两个参数，调用HmacSHA256哈希函数来获得哈希值。
    2. 将此哈希值用base-64编码，得到的值作为此次接口调用的数字签名。

 ```
    lCMAWsZJp9GHIw7W47xnjTJrIb80BjNJ8CgAFlFKhF8=
 ```

5. 签名完成，将生成的数字签名加入到请求里

- 示例

###### Request

```
{
    "action": "req", 
    "ch": "auth",
    "params": {
        "apiKey": "0cxxxxxx-xxxxxx-xxxxxx-xxxx",
        "signatureMethod": "HmacSHA256",
        "signatureVersion": "1.0",
        "timestamp": "1611114854606",
        "signature": "gFD4gepvuViRqrtnycGRDF42y0WT40FaIQXghNGS5Rg="
    }
}
```

###### Response

```
{
    "action": "req",
    "code": 200,
    "ch": "auth",
    "data": {}
}
```
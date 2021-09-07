## gateway_invoke

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/gateway/readme)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `service` —— 服务名，请先在后台配置；
* `api` —— 接口地址，根据后台配置的接口地址进行适配；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `params` —— 需要转发的 GET 参数；
* `headers` —— 需要转发的 HTTP 头部；
* `data` —— 需要转发的 POST 数据；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.gateway_invoke(
    service='metagenomes', api='/api/get_user', data=json.dumps({"user_id": "xxxxxxxxxxx"}))
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json

```


## image_upload

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/service/ossimage)

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `allow_exif` —— 布尔型；是否允许保存图片 exif 值；默认值：false；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.image_upload(image_path='/home/xiangji/Desktop/1.png', allow_exif=True)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "md5": "0a8bf445b3ba3144f1466f8326a6277f",
    "size": 8820,
    "url": "https://image.omgut.com/182/1822106286a7a0eb2f6d742dc2d4d2b0.png"
}
```


## sms

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/service/sms)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `template` —— 短信模板；
* `mobiles` —— 手机号，逗号分割多个手机号；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.sms(
    template='research_download_notice', mobiles='17665342277',
    org_name='测试短信', project_name='科研调查', applied_date='2019-06-01 11:20',
    expiry_date='2019-06-11 11:20')
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json

```


## sts_token

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/service/upload)


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.sts_token()
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "endpoint": "https://oss-cn-shenzhen.aliyuncs.com",
    "destination": "DUS-19198654965-6n6nTj4nHZXsRQAabaqA1e0tq497WsWuiYC6NusT/20210907TZ-3faf9ca95c1d4ccd91efe8236a254a93",
    "base_uri": "https://bge-developer.oss-cn-shenzhen.aliyuncs.com/DUS-19198654965-6n6nTj4nHZXsRQAabaqA1e0tq497WsWuiYC6NusT/20210907TZ-3faf9ca95c1d4ccd91efe8236a254a93",
    "bucket": "bge-developer",
    "credentials": {
        "access_key_secret": "Gt2PNk8uUXhWA5CSs6vvw9QPK3BJEjUqU3HSKpWTrQSH",
        "access_key_id": "STS.NV5Ph5AVB3hLkKh78kgEDYUY2",
        "expiration": "2021-09-07T09:20:51Z",
        "security_token": "CAIShgV1q6Ft5B2yfSjIr5WAG9KBrIljhKqnaW3Z0zg+a8potpDy0Dz2IHBEfnBqCOkcvvsylGhV6f0elqZfdqQAHB2dPJsus8gGr175+CkULx/yv9I+k5SANTW5rXWZtZag6YybIfrZfvCyEQ6m8gZ43br9cxi7QlWhKufnoJV7b9MRLH/aCD1dH4VuOxdFos0XPmezUPG2KUzFj3b3BkhlsRYGQQodj56y2cqB8BHToUTnw+sO3eTLL4OjctNnMeWUOrVdteV9bfjGyzUCqUoIpq15gelI9CnKutaFDkMWzyi9drOFq4w/clIlN/ZnXvBC8v7Al6F+mt7jjL7O4h9HNPh8CimHWJn8kZT7A9y0N+cSK5DmIEiKiIjVb8Gk61wYUzdAOgpEKtEoeyJ7UBBwQTrWe/aq9l2aOFz9QvLYjKhnit03vd6Bn7amKl6eOev7tQ8TJp47aW4xKhcSxhaPW6QacgtKASUFYrGOVtdLcQx5o6HlthGwMyp71SN4suHZbfHbsbxlo+ydOKhLyo0Afp9LnnI3RlDsMdKUh1wTaXZuTMS7ucsHUJa08+2C2/7BI7yEWPoItxBWfC7cqy2VRGkXARDKo4RyMAvIpZmNnfKRts1mTg0S5IxZLTO1auxUhlVs6rKbthnL7Pa/Ay+V5VUl++jzoa9S8ncjJK/+2rfD5mHijjnLb6A3yczeCTBkGBjrcHd1kamfiH9X/UtfmjvpZx9OsBPTkiSSBJRGi63amysUXP8JwLqIE22akz8+WY7T0dEiQvh/ee1CaPG40Dxyy+fvxx/K4N2R604/NreuJ+R7M9YVXEmv+t+2d91TgeZ4Ey67daNCp49Z3xSNz76QUjXW02VRGoABOmDR/Iqo4w8qQk0jNkrivVrJspw4SLASUjR1iF9YEj2z+bIWJiZVPpErjzFgqdiG1RfKwAoTJVxJM9yXUcwxAtvdOQldyJ8dFR+yH6a8lskcKnht+0VC5YtkDn+KEJuLm1PC6RRv87vSWR7m/IhsWo694rZj2ahQDLVGK0+4VEQ="
    }
}
```


## sign_url

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/service/signurl)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `object_name` —— OSS 对象；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `region` —— 区域，可选值：domestic、international；
* `expiration_time` —— 下载地址过期时间，单位：秒；默认值：600（秒）；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.sign_url(
    object_name='ods/microbiome/processed/profile/e1863.a1863.100.1571133531699.855babe0.E-F19581820449.rxn.relab.tsv',
    region='domestic', expiration_time=3600)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "url": "https://international-file.omgut.com/ods%2Fmicrobiome%2Fprocessed%2Fprofile%2Fe1863.a1863.100.1571133531699.855babe0.E-F19581820449.rxn.relab.tsv?Expires=1573026921&Signature=XlYJTft3WyDMZAp5RRxJqp4v89I%3D&OSSAccessKeyId=STS.NQU74xZgz8R8mgc2RR7cQpwhx&security-token=CAISjgN1q6Ft5B2yfSjIr5LgfI7Mt7hbj5DTb0HS1lIHO%2Bx9n7LDmjz2IHBEfnBqCOkcvvsylGhV6f0elqZfdqQAHB2UMJcttM4GqFz5nR8GLEfwv9I%2Bk5SANTW5tXeZtZag24ybIfrZfvCyER%2Bm8gZ43br9cxi7QlWhKufnoJV7b9MRLG7aCD1dH4V5KxdFos0XPmerwJ%2FPVCTnmW3NFkFllxNhgGdkk8SFz9ab9wDVgS8So40Dro%2FqcJ%2B%2FdJsubtUtWdi4meB7aKfF1zZd8V9N%2BLwxia1P4zDNv9aYDh5J%2BRKNPvHP%2F9EoNBV%2BaKk%2BFulJ9aiizrtx47yNzMKuk04LZLwKCn2EH937mZWVSaX5a4szfLz2YzLgl%2F7WZ8Sl6lN%2BOS5HZUVQa9xnMHJ0ABZqVirECNf%2BpQmbM1r7G%2FbdivhogcIv9Tiyo4rWfWroaq6CzCMVNqU7a04VLBMM1QTjCPRWI1YVKQI%2BXebKENUrMU8F9bmT5hfeEzVp1G1G%2BvHzef7SvbgSc5V15R%2B2Cy6sDhqAAaGtJtVgCSKUeuwpLclibtS3R9Lz67bJx529mac%2FlF%2Fm3UzG2VzbOo9A7u0ki%2Fz804XMTXUbzcpg4mznddj0spBDTAIIUo2gxwJBB7xoYUu%2FBRxCIM7khupOcEkC6G9PXSu9HrnhASVAupGuJewFomj%2FMBokCVUv7pVbAErEqkwz",
    "expires": "1573026921"
}
```


## shorturls

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/service/signurl)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `url` —— 要转为短网址的链接；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.shorturls('https://api.private.omgut.com/doc')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "short_url": "https://2i1i.cn/UouT",
    "expires": 604799
}
```


## bgicoin_withdraw

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/service/bgicoin)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `account_name` —— 付款的华大员工邮箱前缀；
* `amount` —— 付款金额，必须大于 0；
* `order_type` —— 订单类型，消费类型: 4线上消费，5体检，6线下消费；
* `order_id` —— 第三方订单编号，需保证在第三方系统中唯一；订单号长度需大于或等于 8


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.bgicoin_withdraw(
    account_name='xiangji', amount=0.01, order_type=4, order_id='436666542')
print(result.dumps(indent=4))
```

```json
{
    "order_id": "436666542",
    "trade_no": "1435163710585004033"
}
```



## wechat_token

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/service/wechat)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `app_id` —— BGE 微信公众号、小程序的 app_id；
* `action` —— 可选项 get、refresh；；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.wechat_token(app_id='demo', action='get')
print(result.dumps(indent=4))
```

```json
{
    "access_token": "4456548ddb4c4fe78b403a4ad554a001"
}
```
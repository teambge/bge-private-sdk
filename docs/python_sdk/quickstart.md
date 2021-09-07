# 快速开始

BGE 私有服务统一使用“签名”方式进行认证，对内对外提供安全的接口访问方式。

详情请参考私有平台文档 [https://api.private.omgut.com/doc](https://api.private.omgut.com/doc) 。


## ENDPOINTS

BGE 私有平台提供了如下可用的 `endpoint`。

| endpoint                    | 解释                                                        |
| --------------------------- | ----------------------------------------------------------- |
| https://api.private.omgut.com‌ | **线上环境** 主域名地址                                     |


## 使用示例

### \_\_init\_\_

直接初始化 `PrivateAPI` 对象

![args](https://img.shields.io/badge/请求参数-args-blue)

* `app_key` —— 系统提供的具有唯一性且能标识客户端身份的字符串；
* `app_secret` —— 加密签名字符串和服务器端验证签名字符串的密钥；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `endpoint=https://api.private.omgut.com‌` —— 平台服务基础地址
* `max_retries=3` —— 最大重试次数
* `timeout=18` —— 接口请求超时时间
* `verbose=False` —— 开启日志输出

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
from private_sdk import PrivateAPI

app_key = 'F4QPfredao9slVB2ua4vVeOryOHsSsC62wM1TUmm'
app_secret = 'kErUUQb5fkaNhCNwoloRMZM8BCbBK4gZiiwljB7wJ4p3xsH24Ma8k2UFAouFyUHZBRqB73fMrMYLK7oOcqjxXViWCHZYxCc56L5D0UQfcBgxXixy9pMDh3YusnUDAcsG'
endpoint = 'https://api.private.omgut.com'

private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=60, verbose=False)

user = private.get_user(biosample_id='E-B19137107158')
print(user.json())
```
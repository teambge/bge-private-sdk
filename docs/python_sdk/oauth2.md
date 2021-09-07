## oauth2_application

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/oauth2/application)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `client_id` —— 开放平台客户端 client_id；
* `redirect_uri` —— 回调地址；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.oauth2_application(
    client_id='ex8FoZjiSmjAlbg0XiqGmaTSIT3SGxoJYnslDGqB',
    redirect_uri='http://test.cn')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "authorization_grant_type": "authorization-code",
    "name": "测试应用",
    "wxmp_app_id": "",
    "redirect_uri": "http://test.cn",
    "client_id": "ex8FoZjiSmjAlbg0XiqGmaTSIT3SGxoJYnslDGqB",
    "client_type": "confidential",
    "description": "",
    "scopes": [
        {
            "message": "读取头像、用户名、昵称以及性别等基本用户信息",
            "title": "基本信息",
            "scope": "profile.default"
        },
        {
            "message": "读取用户编号等其他基本用户信息",
            "title": "增强基本信息",
            "scope": "profile.advanced"
        },
        {
            "message": "读取全部 dbSNP RS 编号的变体分型信息",
            "title": "基因组变体（按 RS 编号）",
            "scope": "variant.rsid"
        },
        {
            "message": "读取全部坐标变体分型信息",
            "title": "基因组变体（按坐标）",
            "scope": "variant.chr"
        },
        {
            "message": "读取样品编号、样品状态、采样时间等信息",
            "title": "读取样品信息",
            "scope": "sample.default:read"
        },
        {
            "message": "写入样品测序数据、采样时间等元信息",
            "title": "补充样品信息",
            "scope": "sample.default:write"
        },
        {
            "message": "读取通过 BGE 研究所或体检问卷提交的表型信息",
            "title": "表型信息",
            "scope": "survey.default"
        },
        {
            "message": "读取微生物样品的类群丰度、功能丰度或基因丰度等",
            "title": "微生物丰度",
            "scope": "abundance.default"
        },
        {
            "message": "读取基于组学数据或表型数据，在第三方开发者部署在 BGE 的模型运算后的解读结果",
            "title": "调用解读模型",
            "scope": "model.default"
        },
        {
            "message": "部署或回滚 BGE 的模型",
            "title": "部署或回滚解读模型",
            "scope": "model.default:write"
        },
        {
            "message": "下载你存储在开放平台的文件，可能包括 PDF 解读报告或者报告相关的图片等文件",
            "title": "文件下载",
            "scope": "service.file:read"
        },
        {
            "message": "上传文件到开放平台",
            "title": "文件上传",
            "scope": "service.file:write"
        },
        {
            "message": "数据项是开放平台的最小数据单元，读取以下数据元集合的数据项",
            "title": "读取数据项",
            "scope": "data_item.default"
        }
    ],
    "logo": ""
}
```


## oauth2_authorize

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/oauth2/authorize)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `client_id` —— 开放平台客户端 client_id；
* `redirect_uri` —— 回调地址；
* `auth_token` —— 用户授权令牌；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `biosample_ids` —— 选中的授权样品信息，JSON 格式字符串；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.oauth2_authorize(
    client_id='uIwrirBQhNFzOVW5uidDvhXHE3Cq403Ml8n2584z',
    auth_token='dKXFoWLtcYAiE9G0uEYKfDLXNrOjtm',
    redirect_uri='http://test.cn',
    biosample_ids=[{"biosample_id": "E-F19955300137", "type": "Lowpass"}])
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "redirect_uri": "pages/index/index",
    "wxmp_app_id": "321",
    "code": "OYUdx9ZvxX11EFJhhpzU6xzyNsJBxD"
}
```


## oauth2_grants

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/oauth2/grants)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `auth_token` —— 用户授权令牌；
* `redirect_uri` —— 回调地址；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `client_id` —— 开放平台客户端 client_id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.oauth2_grants(
    auth_token='a7WkhOsaMCzsTWW9euCntjyWs8x7qn', client_id='ex8FoZjiSmjAlbg0XiqGmaTSIT3SGxoJYnslDGqB')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "biosample_ids": [
        {
            "type": "Lowpass",
            "biosample_id": "E-S13624792132"
        },
        {
            "type": "Full",
            "biosample_id": "E-B13624792132"
        }
    ],
    "grant_time": "2021-03-19 07:00:41",
    "application": {
        "client_id": "84CyOIuRi02ECbp1t9t688NPsBLSoRU6NtJkL5I8",
        "logo": "http://localhost:8000/test.jpg",
        "name": "测试应用"
    }
}
```


## oauth2_revoke_grant

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/oauth2/revoke)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `auth_token` —— 用户授权令牌；
* `client_id` —— 开放平台客户端 client_id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.oauth2_revoke_grant(
    auth_token='a7WkhOsaMCzsTWW9euCntjyWs8x7qn',
    client_id='ex8FoZjiSmjAlbg0XiqGmaTSIT3SGxoJYnslDGqB')
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
```
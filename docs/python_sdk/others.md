## task_result

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/task)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `task_id` —— 任务 id;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.task_result('69909614-9e77-4fbd-b437-4f5b284e3dcc')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "status": "SUCCESS",
    "result": [
        "https://bge-developer.oss-cn-shenzhen.aliyuncs.com/DUS-12345678912-F4QPfredao9slVB2ua4vVeOryOHsSsC62wM1TUmm/20210829TZ-2bb87999f5e646f589598976a51914a0/E-B19137107158_233_1630209166.vcf.gz.tbi",
        "https://bge-developer.oss-cn-shenzhen.aliyuncs.com/DUS-12345678912-F4QPfredao9slVB2ua4vVeOryOHsSsC62wM1TUmm/20210829TZ-2bb87999f5e646f589598976a51914a0/E-B19137107158_233_1630209166.vcf.gz"
    ]
}
```


## survey_projects

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/others/project)

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `project_ids` —— 项目编号，逗号分割多个；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.survey_projects(project_ids='P-W19126783988')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "limit": 50,
    "total": 1,
    "result": [
        {
            "project_id": "P-W19126783988",
            "comment": "低深度全基因组",
            "release_survey_id": 5
        }
    ],
    "count": 1,
    "page": 1,
    "pages": 1
}
```

## survey_target

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/others/target)

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `AND` —— “与逻辑”的筛选条件；
* `OR` —— “或逻辑”的筛选条件；
* `limit` —— 每页返回数量;
* `page` —— 当前页；

**注意**： 当同时提供 concept_code 和 content时，以 concept_code 为主，忽略 content；concept_code 和 content 必须提供其中之一；



![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.survey_target(AND=[
        {
            "data_element_identifier_de": "50d78d39-baf7-43c7-aab1-52704b9ab180",
            "operator": "=",
            "concept_code": "c1"
        }
    ])
print(result)
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "total": 1,
    "page": 1,
    "count": 1,
    "limit": 50,
    "pages": 1,
    "result": [
        {
            "user_id": "00000000000000000001"
        }
    ]
}
```


## question_size

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/others/question_size)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `user_id` ——用户 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.question_size('5c033e04f89dd15e44d48b7d')
print(result)
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
Model({'total': 22})
```


## wechat_profile

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/others/wechat)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `user_id` —— 用户 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.wechat_profile('5c033e04f89dd15e44d48b7d')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "openid": {
        "home": "oyrEv5Qpn4dQTt-CAYZ8vMFmFl94",
        "wgs": "oemn74iTBGzLMAX5D8Pgl-P1zXCA",
        "bger": "oc9_-1MsHmeM4jC18RT2xbiO1WwY"
    },
    "nickname": "刘小姐"
}
```
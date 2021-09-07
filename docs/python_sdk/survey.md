## get_surveys

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/surveys/readme)

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `survey_ids` —— 问卷 id，逗号分割多个 id；
* `developer_ids` —— 开发者用户 id，逗号分割多个 id；
* `sort` —— 以某字段排序，默认升序，字段前加上 “-” 代表降序；可排序字段为：developer_id、survey_id；
* `page` —— 当前页，默认 1；
* `limit` —— 每页数量，默认 50；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.get_surveys(
    sort='-survey_id', page=1, limit=3)
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "survey_id": 215,
    "developer_id": "adea430c-231f-4ee5-9076-aacb08875403",
    "title": "携带者筛查专项致病变异 Sanger 测序验证申请",
    "description": "携带者筛查专项致病变异 Sanger 测序验证申请携带者筛查专项致病变异 Sanger 测序验证申请",
    "end_text": "谢谢参与",
    "redirect_url": "https://pptfapi.omgut.com/common-landing?page_url=/researchPackages/pages/research/completeSurvey/completeSurvey",
    "create_time": "2021-09-03T22:42:00Z",
    "update_time": "2021-09-03T22:42:00Z",
    "question_count": 4
}
{
    "survey_id": 214,
    "developer_id": "5fe882ed-486f-4158-add9-139c7f91a18e",
    "title": "年中聚餐",
    "description": "很久没有一起吃饭了，暂定下周凯悦酒店自助餐。请大家选择合适的时间。",
    "end_text": "谢谢参与",
    "redirect_url": "https://pptfapi.omgut.com/common-landing?page_url=/researchPackages/pages/research/completeSurvey/completeSurvey",
    "create_time": "2021-08-06T17:03:00Z",
    "update_time": "2021-08-06T17:03:00Z",
    "question_count": 1
}
{
    "survey_id": 213,
    "developer_id": "adea430c-231f-4ee5-9076-aacb08875403",
    "title": "疾病病史",
    "description": "疾病史疾病史疾病史疾病史疾病史疾病史疾病史",
    "end_text": "谢谢参与",
    "redirect_url": "https://pptfapi.omgut.com/common-landing?page_url=/researchPackages/pages/research/completeSurvey/completeSurvey",
    "create_time": "2021-06-04T11:03:00Z",
    "update_time": "2021-06-04T11:07:00Z",
    "question_count": 2
}
```


## surveys_retrieve

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/surveys/detail)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `survey_id` —— 问卷 id;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.surveys_retrieve(215)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "survey_id": 215,
    "developer_id": "adea430c-231f-4ee5-9076-aacb08875403",
    "title": "携带者筛查专项致病变异 Sanger 测序验证申请",
    "description": "携带者筛查专项致病变异 Sanger 测序验证申请携带者筛查专项致病变异 Sanger 测序验证申请",
    "end_text": "谢谢参与",
    "redirect_url": "https://pptfapi.omgut.com/common-landing?page_url=/researchPackages/pages/research/completeSurvey/completeSurvey",
    "create_time": "2021-09-03T22:42:00Z",
    "update_time": "2021-09-03T22:42:00Z",
    "question_count": 4
}
```

## survey_replace

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/surveys/replace)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `developer_id` —— 开发者 id；
* `title` —— 标题；
* `description` —— 问卷描述；
* `redirect_url` —— 问卷填写完成后跳转的链接；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `survey_id` —— 问卷 id；
* `end_text` —— 结束语；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.survey_replace(
    developer_id='xj', title='问卷测试', description='测试问卷的描述内容',
    redirect_url='http://www.baidu.com')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "survey_id": 216,
    "developer_id": "xj",
    "title": "问卷测试",
    "description": "测试问卷的描述内容",
    "end_text": null,
    "redirect_url": "http://www.baidu.com",
    "create_time": "2021-09-06T10:30:34Z",
    "update_time": "2021-09-06T10:30:34Z",
    "question_count": 0
}
```


## survey_async

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/surveys/publish)

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `survey_id` —— 问卷 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.survey_async(survey_id='216')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "task_id": "c0b1b9e7-7bf1-4078-a216-fe2f4e95d4a0"
}
```


## survey_delete

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/surveys/delete)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `survey_ids` —— 问卷 id，逗号分割多个 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.survey_delete(survey_ids='216')
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
```


## survey_question

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/questions/readme)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `survey_id` —— 问卷 id；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `question_ids` —— 问题 id，逗号分割多个 id；
* `data_element_identifier_des` —— 数据元编号，逗号分割多个；
* `sort` ——以某字段排序，默认升序，字段前加上 “-” 代表降序；可排序字段为：question_id、survey_id、data_element_identifier_de、required、order、qtype；
* `page` —— 当前页，默认 1；
* `limit` —— 每页数量，默认 50；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.survey_question(215)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "pages": 1,
    "result": [
        {
            "survey_id": 215,
            "question_id": 20042,
            "data_element_identifier_de": "BDE99.00.008.81",
            "order": 0,
            "required": true,
            "title": "建议进行 Sanger 测序验证的致病/疑似致病变异",
            "description": "参考内部性能验证数据集，携带者专项对检出的致病位点划定了严格的“高质量阳性”质控标准。使用该标准，以上列出判断为“低质量阳性”，建议进行 Sanger 测序验证，以确认其真实性，科学指导备孕。",
            "qtype": "textarea",
            "options": []
        },
        {
            "survey_id": 215,
            "question_id": 20043,
            "data_element_identifier_de": "BDE99.00.008.82",
            "order": 1,
            "required": true,
            "title": "预计费用",
            "description": "已包含采血及 Sanger 验证服务过程中所有费用，在华大优康现场支付，支持使用华大币",
            "qtype": "number",
            "options": []
        },
        {
            "survey_id": 215,
            "question_id": 20044,
            "data_element_identifier_de": "BDE99.00.008.83",
            "order": 2,
            "required": true,
            "title": "预约采血日期及时间",
            "description": "现场服务容量限制，请您按照预约时间前往以获得更好的体验。\n采血地点：深圳盐田区深盐路2028号大百汇生命健康产业园 1A 栋 11 楼优康门诊",
            "qtype": "radio",
            "options": [
                {
                    "option_id": 970594,
                    "question_id": 20044,
                    "concept_code": "BCV99.00.024.45",
                    "value": "2021-09-28（星期二）8:30-11:30",
                    "order": 0
                },
                {
                    "option_id": 970595,
                    "question_id": 20044,
                    "concept_code": "BCV99.00.024.46",
                    "value": "2021-09-28（星期二）14:00-17:00",
                    "order": 1
                },
                {
                    "option_id": 970596,
                    "question_id": 20044,
                    "concept_code": "BCV99.00.024.47",
                    "value": "2021-10-12（星期二）8:30-11:30",
                    "order": 2
                },
                {
                    "option_id": 970597,
                    "question_id": 20044,
                    "concept_code": "BCV99.00.024.48",
                    "value": "2021-10-12（星期二）14:00-17:00",
                    "order": 3
                }
            ]
        },
        {
            "survey_id": 215,
            "question_id": 20045,
            "data_element_identifier_de": "BDE99.00.008.85",
            "order": 3,
            "required": true,
            "title": "申请人名字",
            "description": "请填写您的真实姓名",
            "qtype": "input",
            "options": []
        }
    ],
    "total": 4,
    "page": 1,
    "limit": 50,
    "count": 4
}
```


## questions_retrieve

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/questions/detail)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `问题 id；` —— 开发者 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.questions_retrieve(20045)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "survey_id": 215,
    "question_id": 20045,
    "data_element_identifier_de": "BDE99.00.008.85",
    "order": 3,
    "required": true,
    "title": "申请人名字",
    "description": "请填写您的真实姓名",
    "qtype": "input",
    "options": []
}
```


## questions_replace

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/questions/replace)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `survey_id` —— 问卷 id；
* `question_id` —— 问题 id；
* `data_element_identifier_de` —— 数据元编号；
* `title` —— 问题标题；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `qtype` —— 问题类型；
* `order` —— 顺序号；
* `required` —— 是否必填，默认 false；
* `description` —— 问题描述；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.questions_replace(
    survey_id=217, title='测试问卷中的问题', data_element_identifier_de='xxxxxx', 
    question_id=1)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "survey_id": 217,
    "question_id": 1,
    "data_element_identifier_de": "xxxxxx",
    "order": 0,
    "required": true,
    "title": "测试问卷中的问题",
    "description": null,
    "qtype": "input",
    "options": []
}
```


## questions_delete

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/questions/delete)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `question_ids` ——问题 id，逗号分割多个 id；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.questions_delete(question_ids='51,52')
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json

```


## questions_clean

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/questions/clean)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `survey_ids` —— 问卷 id，逗号分割多个 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.questions_clean(survey_ids='217')
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json

```


## survey_options

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/options/readme)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `question_id` —— 问题 id；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `option_ids` —— 选项 id，逗号分割多个 id；
* `sort` —— 以某字段排序，默认升序，字段前加上 “-” 代表降序；可排序字段为：option_id、question_id、concept_code、value；
* `page` —— 当前页，默认 1；
* `limit` —— 每页数量，默认 50；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.survey_options(question_id=20044)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "pages": 1,
    "result": [
        {
            "option_id": 970594,
            "question_id": 20044,
            "concept_code": "BCV99.00.024.45",
            "value": "2021-09-28（星期二）8:30-11:30",
            "order": 0
        },
        {
            "option_id": 970595,
            "question_id": 20044,
            "concept_code": "BCV99.00.024.46",
            "value": "2021-09-28（星期二）14:00-17:00",
            "order": 1
        },
        {
            "option_id": 970596,
            "question_id": 20044,
            "concept_code": "BCV99.00.024.47",
            "value": "2021-10-12（星期二）8:30-11:30",
            "order": 2
        },
        {
            "option_id": 970597,
            "question_id": 20044,
            "concept_code": "BCV99.00.024.48",
            "value": "2021-10-12（星期二）14:00-17:00",
            "order": 3
        }
    ],
    "total": 4,
    "page": 1,
    "limit": 50,
    "count": 4
}
```


## options_retrieve

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/questions/detail)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `question_id` —— 问题 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.options_retrieve(option_id=970594)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "option_id": 970594,
    "question_id": 20044,
    "concept_code": "BCV99.00.024.45",
    "value": "2021-09-28（星期二）8:30-11:30",
    "order": 0
}
```


## options_replace

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/options/replace)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `question_id` —— 问题 id；
* `concept_code` —— 选项系统编号；
* `value` —— 值；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `option_id` —— 选项 id；
* `order` —— 顺序，默认 0；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.options_replace(question_id=51, concept_code='xxxxxxx', value='test')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "option_id": 47,
    "question_id": 107,
    "concept_code": "c3",
    "value": "Ricky.Pagac39",
    "order": 1
}
```


## options_delete

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/options/delete)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `option_ids` —— 选项 id，逗号分割多个 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.options_delete(option_ids='51,52')
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json

```


## options_clean

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/options/clean)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `option_ids` —— 选项 id，逗号分割多个 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.options_clean(option_ids='51,52')
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json

```


## options_batch_create

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/options/batch_create)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `question_id` —— 问题 id；
* `options` —— 选项数据，json 格式参数示例：[{"concept_code": "c1","value": "中国", "order": 10},{"concept_code": "c1","value": "美国"}]；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.options_batch_create(
    question_id=51, 
    options=[{
        "concept_code": "c1", "value": "中国", "order": 10},
        {"concept_code": "c1", "value": "美国"}
])
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json

```


## release_surveys

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/release_surveys/readme)

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `survey_ids` —— 问卷 id，逗号分割多个 id；
* `developer_ids` —— 开发者用户 id，逗号分割多个 id；
* `release_survey_ids` —— 已发布问卷 id，逗号分割多个 id；
* `limesurvey_ids` —— 底层问卷系统 limesurvey 的问卷 id，逗号分割多个 id；
* `sort` —— 以某字段排序，默认升序，字段前加上 “-” 代表降序；可排序字段为：release_survey_id、developer_id、survey_id、limesurvey_id、version、release_time；
* `page` —— 当前页，默认 1；
* `limit` —— 每页数量，默认 50；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.release_surveys(release_survey_ids='536,537')
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "release_survey_id": 537,
    "developer_id": "c71bc0e1-d8b8-4b54-a97c-e417c9d2b7e3",
    "title": "2型糖尿病风险自评量表",
    "description": "糖尿病是危害居民健康的主要慢性非传染性疾病之 一，具有致死、致残的可能，我国已经超过印度成为世 界糖尿病流行中心，糖尿病已经成为我国亟待解决的一 项重大公共卫生问题。由于 2 型糖尿病早期多无特 异症状，临床确诊前约有 9~12 年的潜隐期，适当的生活方式和饮食干预可以预防和延缓糖尿病高危人群进一步发展为糖尿病。通过问卷评估糖尿病患病风险是一种无创、灵敏、可靠、简便、易行的糖尿病筛查方法，可用于预测糖尿病患病风险，区分和筛选高危人群，从而提高未诊断糖尿病的检出率，降低现场筛查的成本，有效节约卫生资源。",
    "end_text": "谢谢参与",
    "redirect_url": "https://pptfapi.omgut.com/common-landing?page_url=/researchPackages/pages/research/completeSurvey/completeSurvey",
    "question_count": 10,
    "survey_id": 187,
    "limesurvey_id": 443524,
    "release_time": "2021-03-09T22:18:03Z",
    "sync_time": "2021-09-03T18:04:48Z",
    "version": 10,
    "survey_url": "https://wj-pro.omgut.com/index.php?r=survey/index&sid=443524&lang=zh-Hans&newtest=Y"
}
{
    "release_survey_id": 536,
    "developer_id": "73387ecd-b9c1-4100-83f5-d28cc8c24dc4",
    "title": "噬菌体靶向肠道共生菌干预肥胖探索",
    "description": "《噬菌体靶向肠道共生菌干预肥胖探索项目》是华大研究院精准健康研究所病原组学研究中心噬菌体抗菌新应用项目组的一个重点项目。\n肠道菌群是肥胖发生的全新的致病因素，目前已经聚焦部分肠道共生菌的变化与肥胖间具有联系。能否筛选特异性抑制／清除这些致胖菌种的噬菌体，用于肥胖患者的个体化干预？\n针对这个科学问题，我们拟通过大样本人群粪便样本大规模筛选靶向致胖菌种的安全有效的噬菌体，评估噬菌体干预肥胖效果及安全性，并进行初步临床探索，尝试针对含有高丰度致胖菌种的肥胖患者进行噬菌体个体化干预。\n本项目将极大填补目前肠道菌群调节的空白，为肥胖干预开辟全新的方向和研究领域，并辐射带动其他代谢性疾病乃至慢性非传染性疾病的干预治疗策略，具有重大引领性价值。",
    "end_text": "谢谢参与",
    "redirect_url": "https://pptfapi.omgut.com/common-landing?page_url=/researchPackages/pages/research/completeSurvey/completeSurvey",
    "question_count": 14,
    "survey_id": 202,
    "limesurvey_id": 548474,
    "release_time": "2021-02-24T17:04:05Z",
    "sync_time": "2021-02-26T17:04:19Z",
    "version": 2,
    "survey_url": "https://wj-pro.omgut.com/index.php?r=survey/index&sid=548474&lang=zh-Hans&newtest=Y"
}
```


## release_surveys_retrieve

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/release_surveys/detail)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `release_survey_id` —— 已发布问卷 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.release_surveys_retrieve(release_survey_id=536)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "release_survey_id": 536,
    "developer_id": "73387ecd-b9c1-4100-83f5-d28cc8c24dc4",
    "title": "噬菌体靶向肠道共生菌干预肥胖探索",
    "description": "《噬菌体靶向肠道共生菌干预肥胖探索项目》是华大研究院精准健康研究所病原组学研究中心噬菌体抗菌新应用项目组的一个重点项目。\n肠道菌群是肥胖发生的全新的致病因素，目前已经聚焦部分肠道共生菌的变化与肥胖间具有联系。能否筛选特异性抑制／清除这些致胖菌种的噬菌体，用于肥胖患者的个体化干预？\n针对这个科学问题，我们拟通过大样本人群粪便样本大规模筛选靶向致胖菌种的安全有效的噬菌体，评估噬菌体干预肥胖效果及安全性，并进行初步临床探索，尝试针对含有高丰度致胖菌种的肥胖患者进行噬菌体个体化干预。\n本项目将极大填补目前肠道菌群调节的空白，为肥胖干预开辟全新的方向和研究领域，并辐射带动其他代谢性疾病乃至慢性非传染性疾病的干预治疗策略，具有重大引领性价值。",
    "end_text": "谢谢参与",
    "redirect_url": "https://pptfapi.omgut.com/common-landing?page_url=/researchPackages/pages/research/completeSurvey/completeSurvey",
    "question_count": 14,
    "survey_id": 202,
    "limesurvey_id": 548474,
    "release_time": "2021-02-24T17:04:05Z",
    "sync_time": "2021-02-26T17:04:19Z",
    "version": 2,
    "survey_url": "https://wj-pro.omgut.com/index.php?r=survey/index&sid=548474&lang=zh-Hans&newtest=Y",
    "release_questions": [
        {
            "release_question_id": 8079,
            "data_element_identifier_de": "BDE99.00.005.61",
            "title": "请同意授权17、18、19 各年（如果有）员工体检结果信息（包括身高、体重、血脂四项结果、员工体检肠道微生物物种丰度和功能丰度信息）",
            "description": null,
            "qtype": "radio",
            "release_options": [
                {
                    "release_option_id": 877521,
                    "concept_code": "BCV99.00.012.15",
                    "code": "A1",
                    "value": "是",
                    "order": 0
                },
                {
                    "release_option_id": 877522,
                    "concept_code": "BCV99.00.012.16",
                    "code": "A2",
                    "value": "否",
                    "order": 1
                }
            ],
            "required": true,
            "order": 0
        },
        {
            "release_question_id": 8080,
            "data_element_identifier_de": "DE02.01.040.00",
            "title": "性别",
            "description": null,
            "qtype": "radio",
            "release_options": [
                {
                    "release_option_id": 877524,
                    "concept_code": "GB/T2261.1.1",
                    "code": "A2",
                    "value": "男",
                    "order": 1
                },
                {
                    "release_option_id": 877525,
                    "concept_code": "GB/T2261.1.2",
                    "code": "A3",
                    "value": "女",
                    "order": 2
                },
                {
                    "release_option_id": 877523,
                    "concept_code": "GB/T2261.1.9",
                    "code": "A1",
                    "value": "未说明的性别",
                    "order": 3
                }
            ],
            "required": true,
            "order": 1
        }
    ]
}
```


## delete_release_surveys

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/release_surveys/delete)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `release_survey_id` —— 已发布问卷 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.delete_release_surveys(release_survey_id=51)
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json

```


## release_questions

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/release_questions/readme)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `release_survey_id` —— 已发布问卷 id；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `release_question_ids` —— 已发布问题 id，逗号分割多个 id；
* `data_element_identifier_des` —— 数据元编号，逗号分割多个；
* `sort` —— 以某字段排序，默认升序，字段前加上 “-” 代表降序；可排序字段为：release_question_id、data_element_identifier_de、required、order、qtype；
* `page` —— 当前页，默认 1；
* `limit` —— 每页数量，默认 50；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.release_questions(release_survey_id=536, data_element_identifier_des='BDE99.00.005.68')
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "release_question_id": 8092,
    "data_element_identifier_de": "BDE99.00.005.68",
    "title": "每次运动时长",
    "description": null,
    "qtype": "radio",
    "release_options": [
        {
            "release_option_id": 877589,
            "concept_code": "BCV99.00.012.34",
            "code": "A1",
            "value": "半小时及以下",
            "order": 0
        },
        {
            "release_option_id": 877590,
            "concept_code": "BCV99.00.012.35",
            "code": "A2",
            "value": "半小时到一小时",
            "order": 1
        },
        {
            "release_option_id": 877591,
            "concept_code": "BCV99.00.012.36",
            "code": "A3",
            "value": "一小时到两小时",
            "order": 2
        },
        {
            "release_option_id": 877592,
            "concept_code": "BCV99.00.012.37",
            "code": "A4",
            "value": "两小时及以上",
            "order": 3
        }
    ],
    "required": true,
    "order": 14
}
```


## release_questions_retrieve

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/release_questions/detail)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `release_question_id` —— 已发布问题 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.release_questions_retrieve(release_question_id=8092)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "release_question_id": 8092,
    "data_element_identifier_de": "BDE99.00.005.68",
    "title": "每次运动时长",
    "description": null,
    "qtype": "radio",
    "release_options": [
        {
            "release_option_id": 877589,
            "concept_code": "BCV99.00.012.34",
            "code": "A1",
            "value": "半小时及以下",
            "order": 0
        },
        {
            "release_option_id": 877590,
            "concept_code": "BCV99.00.012.35",
            "code": "A2",
            "value": "半小时到一小时",
            "order": 1
        },
        {
            "release_option_id": 877591,
            "concept_code": "BCV99.00.012.36",
            "code": "A3",
            "value": "一小时到两小时",
            "order": 2
        },
        {
            "release_option_id": 877592,
            "concept_code": "BCV99.00.012.37",
            "code": "A4",
            "value": "两小时及以上",
            "order": 3
        }
    ],
    "required": true,
    "order": 14
}
```


## survey_responses

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/responses/readme)


![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `response_ids` —— 答卷 id，逗号分割多个 id；
* `user_ids` —— 用户系统 id，逗号分割多个 id；
* `biosample_ids` —— 生物样品编号，逗号分割多个；
* `limeresponse_ids` —— 底层问卷系统 limesurvey 中的答卷编号，逗号分割多个 id；
* `release_survey_ids` —— 已发布问卷 id，逗号分割多个；
* `sort` —— 以某字段排序，默认升序，字段前加上 “-” 代表降序；可排序字段为：response_id、user_id、biosample_id、submit_time、start_time、time_consuming、release_survey_id；
* `page` —— 当前页，默认 1；
* `limit` —— 每页数量，默认 50；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.survey_responses(response_ids='51,52')
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "user_id": "5be85a3e04c0fb5e93c8cca3",
    "biosample_id": "E-B19961155442",
    "time_consuming": null,
    "response_id": 51,
    "ip_address": null,
    "referer_url": null,
    "submit_time": null,
    "start_time": null,
    "last_action_time": null,
    "release_survey_id": 5,
    "limeresponse_id": null
}
{
    "user_id": "5be85a3e04c0fb5e93c8c8e5",
    "biosample_id": "E-B19307463788",
    "time_consuming": null,
    "response_id": 52,
    "ip_address": null,
    "referer_url": null,
    "submit_time": null,
    "start_time": null,
    "last_action_time": null,
    "release_survey_id": 5,
    "limeresponse_id": null
}
```


## responses_retrieve

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/responses/detail)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `response_id` —— 答卷 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.responses_retrieve(response_id=51)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "user_id": "5be85a3e04c0fb5e93c8cca3",
    "biosample_id": "E-B19961155442",
    "time_consuming": null,
    "response_id": 51,
    "ip_address": null,
    "referer_url": null,
    "submit_time": null,
    "start_time": null,
    "last_action_time": null,
    "release_survey_id": 5,
    "limeresponse_id": null
}
```


## import_response

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/responses/import)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `user_id` —— 用户系统 id；
* `biosample_id` —— 生物样品编号；
* `release_survey_id` —— 已发布问卷 id；
* `answers` —— 答卷中的答案；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
answers = [{"release_question_id": 467, "content": "2003-09-29T10:32:28Z" }, {"release_question_id": 468, "concept_code": "c2" }, {"release_question_id": 468, "concept_code": "c3" }]
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.import_response(
                user_id='xxxxxxxxx', biosample_id='E-B123432423',
                release_survey_id=107, answers=answers)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "user_id": "5d6f1f16294e6365bb5a5f58",
    "biosample_id": "E-B19319845838",
    "time_consuming": 14.98,
    "response_id": 99,
    "ip_address": "116.211.5.58",
    "referer_url": null,
    "submit_time": "2019-09-10T23:12:24Z",
    "start_time": "2019-09-10T23:12:11Z",
    "last_action_time": "2019-09-10T23:12:24Z",
    "release_survey_id": 103,
    "limeresponse_id": 85
}
```


## sync_responses

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/responses/sync)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `limesurvey_id` —— 底层问卷 id；
* `limeresponses_id` —— 底层答卷 id；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `user_id` —— 答卷要绑定的用户 id；
* `biosample_id` —— 答卷要绑定的生物样品编号；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.sync_responses(limesurvey_id=5112341, limeresponse_id=51)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "user_id": "5d303c5bf65e0a5b090b7546",
    "biosample_id": null,
    "time_consuming": 559.22,
    "response_id": 55,
    "ip_address": "116.211.5.58",
    "referer_url": null,
    "submit_time": "2019-07-25T00:06:32Z",
    "start_time": "2019-07-24T23:57:15Z",
    "last_action_time": "2019-07-25T00:06:32Z",
    "release_survey_id": 98,
    "limeresponse_id": 1
}
```


## survey_answers

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/answers/readme)

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `response_ids` —— 答卷 id，逗号分割多个 id；
* `release_survey_ids` —— 已发布问卷 id，逗号分割多个 id；
* `answer_ids` —— 答案 id，逗号分割多个 id；
* `user_ids` —— 用户系统 id，逗号分割多个 id；
* `biosample_ids` —— 生物样品编号，逗号分割多个；
* `concept_codes` —— 标准数据定义关联代码（答案内容的关联代码），逗号分割多个；
* `sort` —— 以某字段排序，默认升序，字段前加上 “-” 代表降序；可排序字段为：response_id、user_id、biosample_id、submit_time、start_time、time_consuming、release_survey_id
* `page` —— 当前页，默认 1；
* `limit` —— 每页数量，默认 50；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.survey_answers(answer_ids='51,52')
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "answer_id": 51,
    "concept_code": "CV02.10.005.06",
    "content": "恶性肿瘤",
    "time_consuming": null,
    "release_question": {
        "release_question_id": 97,
        "data_element_identifier_de": "DE02.10.095.00"
    },
    "create_time": "2019-05-10T17:06:21Z",
    "response": {
        "response_id": 2,
        "user_id": "5c033e04f89dd15e44d48b7d",
        "biosample_id": "E-B19799031005",
        "release_survey_id": 5
    }
}
```


## latest_answers

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/answers/latest)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `user_id` —— 用户系统 id；
* `data_element_identifier_des` —— 数据元编号，逗号分割多个；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.latest_answers(user_id='5d649d868a04445685d4dd21', data_element_identifier_des='_CODE_education')
for item in result:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "answer_id": 445,
    "concept_code": "",
    "content": "每天",
    "time_consuming": 2.53,
    "release_question": {
        "release_question_id": 376,
        "data_element_identifier_de": "_CODE_education"
    },
    "create_time": "2019-12-11T19:14:20Z",
    "response": {
        "response_id": 126,
        "user_id": "5d649d868a04445685d4dd21",
        "biosample_id": "E-B19143015708",
        "release_survey_id": 107
    }
},
{
    "answer_id": 446,
    "concept_code": "40444",
    "content": "是",
    "time_consuming": 3.33,
    "release_question": {
        "release_question_id": 375,
        "data_element_identifier_de": "_CODE_education"
    },
    "create_time": "2019-12-11T19:14:20Z",
    "response": {
        "response_id": 126,
        "user_id": "5d649d868a04445685d4dd21",
        "biosample_id": "E-B19143015708",
        "release_survey_id": 107
    }
},
{
    "answer_id": 447,
    "concept_code": "111111111",
    "content": "足球",
    "time_consuming": 6.1,
    "release_question": {
        "release_question_id": 374,
        "data_element_identifier_de": "_CODE_education"
    },
    "create_time": "2019-12-11T19:14:20Z",
    "response": {
        "response_id": 126,
        "user_id": "5d649d868a04445685d4dd21",
        "biosample_id": "E-B19143015708",
        "release_survey_id": 107
    }
}
```


## answers_retrieve

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/answers/detail)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `answer_id` —— 答案 id；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.answers_retrieve(answer_id=51)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "answer_id": 51,
    "concept_code": "CV02.10.005.06",
    "content": "恶性肿瘤",
    "time_consuming": null,
    "release_question": {
        "release_question_id": 97,
        "data_element_identifier_de": "DE02.10.095.00"
    },
    "create_time": "2019-05-10T17:06:21Z",
    "response": {
        "response_id": 2,
        "user_id": "5c033e04f89dd15e44d48b7d",
        "biosample_id": "E-B19799031005",
        "release_survey_id": 5
    }
}
```


## survey_statistics

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/statistics/readme)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `survey_id` —— 问卷编号（未发布问卷的编号）;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.survey_statistics(survey_id=2)
print(result)
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "total_question_size": 7,
    "title": "基因组问卷",
    "readable_avg_completion_time": "1分3秒",
    "questions": [
        {
            "readable_completion_rate": "100%",
            "statistics": {
                "type": "list",
                "answers": [
                    {
                        "create_time": null,
                        "serial": 1,
                        "content": "男",
                        "concept_code": "GB/T2261.1.1",
                        "size": 2739
                    },
                    {
                        "create_time": null,
                        "serial": 2,
                        "content": "女",
                        "concept_code": "GB/T2261.1.2",
                        "size": 3027
                    }
                ]
            },
            "data_element_identifier_de": "DE02.01.040.00",
            "serial": 1,
            "completion_size": 5766,
            "order": 1,
            "title": "性别",
            "completion_rate": 1.0,
            "required": true,
            "qtype": "radio"
        }
        ......
    ],
    "avg_completion_time": 63,
    "total_completion_size": 5766,
    "update_time": "2021-09-06 18:08",
    "description": "BGE 全基因组问卷",
    "completions": [
        {
            "completion_size": 0,
            "date": "2021-08-31"
        },
        {
            "completion_size": 0,
            "date": "2021-09-01"
        },
        {
            "completion_size": 1,
            "date": "2021-09-02"
        },
        {
            "completion_size": 3,
            "date": "2021-09-03"
        },
        {
            "completion_size": 0,
            "date": "2021-09-04"
        },
        {
            "completion_size": 0,
            "date": "2021-09-05"
        },
        {
            "completion_size": 0,
            "date": "2021-09-06"
        }
    ]
}
```


## question_statistics

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/survey/statistics/question)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `survey_id` —— 问卷编号（未发布问卷的编号）；
* `data_element_identifier_de` —— 问题绑定的数据元编号；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `limit` —— 单页返回数，最小值 1，最大值 100；
* `page` —— 页码，大于等于 1；



![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.question_statistics(survey_id=2, data_element_identifier_de='DE04.10.167.00', page=1)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "answers": {
        "pages": 577,
        "total": 5766,
        "result": [
            {
                "create_time": "2021-09-03 03:49:46",
                "serial": 1,
                "size": null,
                "content": 165,
                "concept_code": ""
            },
            {
                "create_time": "2021-09-03 03:42:10",
                "serial": 2,
                "size": null,
                "content": 152,
                "concept_code": ""
            },
            {
                "create_time": "2021-09-03 03:16:28",
                "serial": 3,
                "size": null,
                "content": 165,
                "concept_code": ""
            },
            {
                "create_time": "2021-09-01 16:08:26",
                "serial": 4,
                "size": null,
                "content": 176,
                "concept_code": ""
            },
            {
                "create_time": "2021-08-29 08:49:40",
                "serial": 5,
                "size": null,
                "content": 170.5,
                "concept_code": ""
            },
            {
                "create_time": "2021-08-26 01:16:02",
                "serial": 6,
                "size": null,
                "content": 155,
                "concept_code": ""
            },
            {
                "create_time": "2021-08-25 14:14:55",
                "serial": 7,
                "size": null,
                "content": 170.5,
                "concept_code": ""
            },
            {
                "create_time": "2021-08-25 13:47:25",
                "serial": 8,
                "size": null,
                "content": 166,
                "concept_code": ""
            },
            {
                "create_time": "2021-08-25 13:10:07",
                "serial": 9,
                "size": null,
                "content": 177,
                "concept_code": ""
            },
            {
                "create_time": "2021-08-25 12:03:16",
                "serial": 10,
                "size": null,
                "content": 155,
                "concept_code": ""
            }
        ],
        "page": 1,
        "limit": 10,
        "count": 10
    },
    "summary": {
        "maximum": 192.0,
        "minimum": 0,
        "median": 158.0,
        "average": 105.51
    },
    "type": "dict"
}
```
## openbge_search

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/search/readme)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `query` —— 查询文本;
* `category` —— 类别；可选值：app,report,survey、report、survey、gene、app;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `biosample_id` —— 生物样品编号；
* `limit` —— 每页返回数量;
* `page` —— 当前页；

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.openbge_search(
    query='抵抗力', category='report', limit=2, page=1)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "pages": 1089298,
    "result": [
        {
            "highlight": {},
            "id": "5df3c0ab54a9e750c9683c0f",
            "type": "complex",
            "data": {
                "number": "2900570831C",
                "uTime": 1576255659241.0,
                "name": {
                    "chinese": "高血压",
                    "english": ""
                },
                "category": "report",
                "cTime": 1576255659241.0,
                "id": "5df3c0ab54a9e750c9683c0f",
                "biosample_id": "E-B19615110967",
                "summary": "高血压  (L1-BA0), 以动脉血压持续升高为特征的“心血管综合征”，70%的脑卒中和50%的心肌梗死与高血压有关，20%~30%的高血压发生与先天遗传因素有关，70%~80%的高血压发生与不健康的生活习惯有关 高血压是常见的慢性病，是以动脉血压持续升高为特征的“心血管综合征”，是我国心脑血管病最主要的危险因素，也是我国心脑血管病死亡的主要原因。脑卒中、心肌梗死、心力衰竭及慢性肾脏病等为主要并发症，致残、致死率高。目前我国约有2亿多高血压患者，每10个成年人中有2人患有高血压。当前我国心血管病死亡占总死亡的41%，每年死亡350万，其中70%的脑卒中和50%的心肌梗死与高血压有关。降低高血压患者的血压水平可使脑卒中风险降低40%~50%，使心肌梗死风险降低15%~30%。20%~30%的高血压发生与先天遗传因素有关，70%~80%的高血压发生与不健康的生活习惯有关。来自日本全球健康与医学研究中心、中国上海交通大学和清华大学、美国杜兰大学等6个国家研究人员组成的研究小组通过基因组分析，发现了多个与东亚地区人群高血压相关的易感基因，其中以ALDH2基因影响血压情况最显著。 检测基因为 rs11646213(CDH13)、rs991316(ADH7)、rs2820037(RYR2)、rs2398162(Intergenic)。",
                "reportId": "5df3c08254a9e750c9682ba6",
                "product": "Full"
            },
            "app": "bge_v2"
        },
        {
            "highlight": {},
            "id": "5df2529582dfa4438a47859a",
            "type": "complex",
            "data": {
                "number": "DTJ2017000282",
                "uTime": 1576161943733.0,
                "name": {
                    "chinese": "高血压",
                    "english": ""
                },
                "category": "report",
                "cTime": 1576161941412.0,
                "id": "5df2529582dfa4438a47859a",
                "biosample_id": "E-B19854988933",
                "summary": "高血压  (L1-BA0), 以动脉血压持续升高为特征的“心血管综合征”，70%的脑卒中和50%的心肌梗死与高血压有关，20%~30%的高血压发生与先天遗传因素有关，70%~80%的高血压发生与不健康的生活习惯有关 高血压是常见的慢性病，是以动脉血压持续升高为特征的“心血管综合征”，是我国心脑血管病最主要的危险因素，也是我国心脑血管病死亡的主要原因。脑卒中、心肌梗死、心力衰竭及慢性肾脏病等为主要并发症，致残、致死率高。目前我国约有2亿多高血压患者，每10个成年人中有2人患有高血压。当前我国心血管病死亡占总死亡的41%，每年死亡350万，其中70%的脑卒中和50%的心肌梗死与高血压有关。降低高血压患者的血压水平可使脑卒中风险降低40%~50%，使心肌梗死风险降低15%~30%。20%~30%的高血压发生与先天遗传因素有关，70%~80%的高血压发生与不健康的生活习惯有关。来自日本全球健康与医学研究中心、中国上海交通大学和清华大学、美国杜兰大学等6个国家研究人员组成的研究小组通过基因组分析，发现了多个与东亚地区人群高血压相关的易感基因，其中以ALDH2基因影响血压情况最显著。 检测基因为 rs991316(ADH7)、rs2820037(RYR2)、rs2398162(Intergenic)、rs11646213(CDH13)。",
                "reportId": "5df2528f82dfa4438a478434",
                "product": "Trial"
            },
            "app": "bge_v2"
        }
    ],
    "total": 2178595,
    "count": 2,
    "limit": 2,
    "page": 1
}
```


## create_index

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/search/survey/create)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `type` —— 索引类型，固定设置为 survey;
* `content` —— 索引内容;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.create_index(type='survey', content=[{"id": 111, "title": "标题x", "description": "描述 x", "status": 1, "isPublic": 1, "developerId": "xyz", "developerName": "Tom", "researchPlanId": 1, "planTitle": "痛风", "detailImage": "http://test.com/test.jpg", "listImage": "http://test.com/test.jpg"}])
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "status": 1,
    "isPublic": 1,
    "researchPlanId": 1,
    "title": "标题x",
    "developerId": "xyz",
    "developerName": "Tom",
    "description": "描述 x",
    "detailImage": "http://test.com/test.jpg",
    "id": 111,
    "listImage": "http://test.com/test.jpg",
    "planTitle": "痛风"
}
```


## delete_index

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/search/survey/delete)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `type` —— 索引类型，固定设置为 survey;
* `ids` —— 要删除的问卷索引编号，多个编号以逗号分割;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.delete_index(type='survey', ids='111')
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "deleted": true,
    "id": "111",
    "not_found": false
}
```

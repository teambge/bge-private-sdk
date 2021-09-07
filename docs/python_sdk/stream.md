## stream_range

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/stream/range)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `namespace` —— 命名空间;
* `data_element_id` —— 数据元编号;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `fundamental_entity_id` —— 个体编号，与参数 biosample_id 互斥，且必填两者其中之一；
* `biosample_id` —— 生物样品编号，与参数 fundamental_entity_id 互斥，且必填两者其中之一；
* `start_time` ——流数据生成时间起始时间，支持的日期格式请查看 格式，左闭区间；
* `end_time` —— 流数据生成时间结束时间，支持的日期格式请查看 格式，右闭区间；
* `sort_direction` —— 排序方式，取值范围：asc（升序）、desc（降序）；默认：desc；
* `next_page` —— 下一页参数；
* `limit` —— 一页返回数据量，最大值：100；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.stream_range(
    namespace='BGE_DEVELOPER_PLATFORM', data_element_id='45f69871-7d89-11eb-a38f-00163e0eae20',
    fundamental_entity_id='093f5e9a-7c96-11eb-a38f-00163e0eae20')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "result": [
        {
            "stream_generate_time_mask": "1111-00-00T00:00:00.000000±1111",
            "stream_generate_time": "2017-01-01T00:00:00.000000+0800",
            "data_element": {
                "data_element_name": "Q-T间期",
                "data_element_id": "45f69871-7d89-11eb-a38f-00163e0eae20",
                "data_element_description": "",
                "data_element_source_domain": "BGI_DATA_ELEMENT",
                "data_element_source_id": "4.3.11.0"
            },
            "stream_data": {
                "status": "final",
                "value_quantity": {
                    "unit": "ms",
                    "value": 356
                },
                "note": [],
                "performer": [
                    {
                        "reference": "bgi_healthfamily",
                        "display": "员工健康计划"
                    }
                ],
                "resource_type": "Observation",
                "interpretation": []
            },
            "stream_meta": {
                "namespace": "BGE_DEVELOPER_PLATFORM",
                "fundamental_entity_id": "093f5e9a-7c96-11eb-a38f-00163e0eae20"
            },
            "create_time": "2021-03-10T10:24:14.650000+0800",
            "stream_id": "b4289d33-8147-11eb-a39e-00163e0eae20",
            "data_type": 2
        }
    ],
    "next_page": null,
    "count": 1
}
```


## write_stream

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/stream/write)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `fundamental_entity_id` —— 个体编号;
* `data_element_id` —— 数据元编号;
* `stream_generate_time` —— 流数据生成时间;
* `stream_data` —— 流数据内容；JSON 格式内容;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `fundamental_entity_id` —— 是否允许重复写入 fundamental_entity_id、data_element_id、stream_generate_time 都相同的数据；默认为 False，不允许重复写入；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.write_stream(
    fundamental_entity_id='76079655-7b07-11eb-a38f-00163e0eae20',
    data_element_id='02393f70-c7e4-11e9-bfed-00163e104c79',
    stream_generate_time='1986', stream_data='{"name": "leo"}',
    duplicate_enabled='true')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
      "stream_id": "552145d6-7cb8-11eb-ad05-00163e0c67a3"
}
```


## batch_write_stream

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/stream/batch_write)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `streams` —— 要写入的数据流数据数组;
* `streams.[0].fundamental_entity_id` —— 个体编号;
* `streams.[0].data_element_id` —— 数据元编号;
* `streams.[0].stream_generate_time` —— 流数据生成时间;
* `streams.[0].stream_data` —— 流数据内容；JSON 格式内容;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
streams = [
        {
            "fundamental_entity_id": "093f5e9a-7c96-11eb-a38f-00163e0eae20",
            "data_element_id": "5c60448e-a0bb-11ea-b57c-48a47299ee4a",
            "stream_generate_time": "1971",
            "stream_data": {
                "name": "leo"
            }
        },
        {
            "fundamental_entity_id": "d268f9e6-7c8e-11eb-8440-48a47299ee4a",
            "data_element_id": "5c60448e-a0bb-11ea-b57c-48a47299ee4a",
            "stream_generate_time": "1971",
            "stream_data": {
                "name": "tom"
            }
        }
    ]
result = private.batch_write_stream(streams, duplicate_enabled='true')
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "is_succeed": true,
    "message": "",
    "stream": {
        "stream_meta": {
            "namespace": "BGE_DEVELOPER_PLATFORM",
            "fundamental_entity_id": "093f5e9a-7c96-11eb-a38f-00163e0eae20"
        },
        "stream_generate_time": "1971-01-01T00:00:00.000000+0800",
        "stream_id": "0a5fb930-0e56-11ec-9d31-00163e0c480e",
        "data_element": {
            "data_element_id": "5c60448e-a0bb-11ea-b57c-48a47299ee4a"
        }
    }
}
{
    "is_succeed": false,
    "message": "fundamental_entity_id 不存在",
    "stream": {
        "stream_meta": {
            "namespace": "BGE_DEVELOPER_PLATFORM",
            "fundamental_entity_id": "d268f9e6-7c8e-11eb-8440-48a47299ee4a"
        },
        "stream_generate_time": "1971-01-01T00:00:00.000000+0800",
        "stream_id": null,
        "data_element": {
            "data_element_id": "5c60448e-a0bb-11ea-b57c-48a47299ee4a"
        }
    }
}
```


## stream_retrieve

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/stream/retrieve)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `stream_id` —— 数据流编号;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.stream_retrieve('b4289d33-8147-11eb-a39e-00163e0eae20')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "stream_generate_time_mask": "1111-00-00T00:00:00.000000±1111",
    "stream_generate_time": "2017-01-01T00:00:00.000000+0800",
    "data_element": {
        "data_element_name": "Q-T间期",
        "data_element_source_id": "4.3.11.0",
        "data_element_description": "",
        "data_element_source_domain": "BGI_DATA_ELEMENT",
        "data_element_id": "45f69871-7d89-11eb-a38f-00163e0eae20"
    },
    "stream_data": {
        "status": "final",
        "value_quantity": {
            "unit": "ms",
            "value": 356
        },
        "note": [],
        "performer": [
            {
                "reference": "bgi_healthfamily",
                "display": "员工健康计划"
            }
        ],
        "resource_type": "Observation",
        "interpretation": []
    },
    "stream_meta": {
        "namespace": "BGE_DEVELOPER_PLATFORM",
        "fundamental_entity_id": "093f5e9a-7c96-11eb-a38f-00163e0eae20"
    },
    "create_time": "2021-03-10T10:24:14.650000+0800",
    "stream_id": "b4289d33-8147-11eb-a39e-00163e0eae20",
    "data_type": 2
}
```


## stream_bind

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/stream/bind)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `biosample_id` —— 生物样品编号;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.stream_bind('E-B19137107158')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "fundamental_entity_id": "594e5bc0-a1bc-11eb-b664-c8b29b0eab1e"
}
```
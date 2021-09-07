## register_batch

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/batch/register)


![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `title` —— 批次标题；
* `intro` —— 批次简介；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.register_batch(title='test_batch', intro='test_batch_intro')
print(result)
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
Model({'batch_no': 1630658571462})
```


## retrieve_batch

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/batch/readme)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `batch_no` —— 批次号;


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.retrieve_batch(1630658571462)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "ctime": "2021-09-03T16:42:51",
    "batch_no": 1630658571462,
    "extracted": false,
    "committed": false,
    "commit_time": null,
    "namespace": "BGE_DEVELOPER_PLATFORM",
    "intro": "test_batch_intro",
    "name": "xj_test_batch"
}
```


## import_batch

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/batch/import)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `batch_no` —— 批次号；
* `data_items` ——待导入的数据项列表；数组中最多允许 100 个子项；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `biosample_id` —— 生物样品编号；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
data_items = [
        {
            "data_element_id": "00011d12-b363-11e9-bfed-00163e104c79",
            "attributes": {
                "deid_idx": "deid-0",
                "age": 18,
                "parents": ["father", "mother"],
                "other": {
                    "notice": "tips"
                }
            }
        },
        {
            "data_element_id": "00011d13-b363-11e9-bfed-00163e104c79",
            "attributes": {
                "deid_idx": "deid-1"
            }
        }
    ]
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.import_batch(1630484655317, data_items, biosample_id='E-F19955300137')
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
```


## commit_batch

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/batch/commit)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `batch_no` ——批次号;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.commit_batch(1630805972180)
print(result)
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
Model({'completed': None, 'progress': 'PENDING', 'result': None, 'task_id': 'bab1d13e-32c4-4890-9ae8-590a9c6cbace', 'task_url': 'http://localhost:8070/openbge/task/bab1d13e-32c4-4890-9ae8-590a9c6cbace'})
```
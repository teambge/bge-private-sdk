## add_collection

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/collection/add-collection)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `collection_name` —— 数据集名称，不超过20个字符;
* `collection_type` —— 类型；取值范围：private、public;
* `collection_omic` —— 组学；取值范围：multiomics、genomics、metagenomics、phenomics、exposomics;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `collection_description` —— 数据集描述，不超过30个字符;
* `data_element_ids` —— 数据元编号，编号之间以空格或换行进行隔开;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.add_collection(collection_name='数据集测试-s', collection_omic='genomics', collection_type='public', collection_description='描述内容')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "collection_id": "C-D21400843387"
}
```


## edit_collection

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/collection/edit-collection)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `collection_id` —— 数据集编号;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `collection_type` —— 类型；取值范围：private、public;
* `collection_omic` —— 组学；取值范围：multiomics、genomics、metagenomics、phenomics、exposomics;
* `collection_description` —— 数据集描述，不超过30个字符;
* `data_element_ids` —— 数据元编号，编号之间以空格或换行进行隔开;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.edit_collection(collection_id='C-D21400843387', collection_type='private', collection_description='修改描述')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "collection_id": "C-D21400843387"
}
```

## collection_detail_or_delete

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/collection/collection-detail)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `collection_id` —— 数据集编号;
* `type` —— detail: 查询数据集详情数据，delete: 删除数据集;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.collection_detail_or_delete('C-D21400843387', 'detail')
print(result.dumps(indent=4))
```

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.collection_detail_or_delete('C-D21400843387', 'delete')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "collection_omic": "genomics",
    "collection_name": "数据集测试-s",
    "collection_description": "修改描述",
    "deids": [],
    "collection_id": "C-D21400843387",
    "collection_type": "private"
}
```

```json
{
    "collection_id": "C-D21400843387"
}
```
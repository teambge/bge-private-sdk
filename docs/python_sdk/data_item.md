## retrieve_data_item

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/data-item/readme)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `data_element_id` —— 生物样品编号;
* `namespace` —— 命名空间;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `biosample_id` —— 每页返回数量;
* `batch_no` —— 批次号，用来获取某个数据元某个旧批次的数据；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.retrieve_data_item('000e1f19-de2c-11ea-a2b3-00163e0eae20', 'KB-BGE')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "biosample_id": "",
    "data_element_id": "000e1f19-de2c-11ea-a2b3-00163e0eae20",
    "namespace": "KB-BGE",
    "batch_no": 1610959565885,
    "attributes": {
        "data_element_source_domain": "omim",
        "defaultId": 2790,
        "items": [
            {
                "backgroundEn": "",
                "cTime": 0,
                "data_element_source_domain": "omim",
                "gene": "LTBP2",
                "geneticMode": "AR",
                "id": 2790,
                "nameCn": "原发性开角型青光眼3D型",
                "nameEn": "Primary Open Angle Glaucoma 3D",
                "omim": "613086",
                "otherName": "Glaucoma 3, Primary Congenital, D; Glc3D",
                "outlines": [],
                "precautions": [],
                "projectIntroduction": "<p>原发性开角型青光眼3D型是原发性开角型青光眼的一种亚型，主要临床表现为出生或幼儿期眼内压力明显增加、大眼球（牛眼）和角膜水肿。它是由于小梁网以及前房角发育缺陷导致的房水引流不畅。</p>",
                "references": [],
                "riskFactors": [],
                "subNameCn": "原发性开角型青光眼3D型",
                "subNameEn": "Primary Open Angle Glaucoma 3D",
                "systemSort": "眼病",
                "treatments": [],
                "uTime": 1597219895000
            }
        ],
        "knowledgeType": "genetic"
    }
}
```


## retrieve_batch_data_item

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/data-item/data-item-batch)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `namespace` —— 命名空间;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `biosample_id` —— 生物样品编号;
* `batch_no` —— 批次号，用来获取某个数据元某个旧批次的数据；
* `next_page` —— 下一页参数;
* `collection_id` —— 数据集编号;
* `data_element_ids` —— 数据元编号列表，逗号分割多个编号;




![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.retrieve_batch_data_item('WGSAI3.0-L-FULL', biosample_id='E-B19340081969',
                                          collection_id='C-D20813389056')
print(result['result'])
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
[<Model object at 0x7ff52397f2b0>, <Model object at 0x7ff52397f2e8>, <Model object at 0x7ff52397f320>, <Model object at 0x7ff52397f358>, <Model object at 0x7ff52397f390>, <Model object at 0x7ff52397f3c8>, <Model object at 0x7ff52397f400>, <Model object at 0x7ff52397f438>, <Model object at 0x7ff52397f470>, <Model object at 0x7ff52397f4a8>, <Model object at 0x7ff52397f4e0>]
```


## data_item_query

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/data-item/query)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `namespace` —— 命名空间;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `biosample_id` —— 生物样品编号;
* `batch_no` —— 批次号;
* `next_page_key` —— 下一页参数；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.data_item_query('WGSAI3.0-L-FULL', biosample_id='E-B19340081969', batch_no='1629820403108')
for item in result['data_items']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "biosample_id": "E-B19340081969",
    "data_element_id": "5ee515db-de29-11ea-a2b3-00163e0eae20",
    "namespace": "WGSAI3.0-L-FULL",
    "batch_no": 1629820403108,
    "attributes": {
        "genetic_result": "暂未发现携带致病突变",
        "research_ethnicity": null,
        "binary_classification_marker": "Negative",
        "genetic_influence": null,
        "bioinformatics": {
            "targeted_variation": {
                "genomic_location": [
                    "chr8:142917215:C>A"
                ],
                "rsid": [
                    "."
                ]
            },
            "variation": [
                {
                    "subject": {
                        "OR_value": null,
                        "risk_genotype": null,
                        "inheritance": "AR",
                        "purpose": null,
                        "P_value": null,
                        "variation_interpretation": "暂未发现携带致病突变"
                    },
                    "HGVS": {
                        "nucleotide": "c.240-1G>T",
                        "molecular_consequence": null,
                        "amino_acid": "_"
                    },
                    "zygosity": "Ref",
                    "sense_antisense": "",
                    "gene": [
                        "CYP11B2"
                    ],
                    "mRNA_version": [
                        "NM_000498.3"
                    ],
                    "rsid": ".",
                    "reference_version": "hg38",
                    "vcf": {
                        "ratio": null,
                        "genotype": "C/C",
                        "depth": null,
                        "QUAL": null,
                        "ref": "C"
                    },
                    "genomic_location": "chr8:142917215:C>A",
                    "metabolism_rate": null,
                    "cytogenetic_location": null,
                    "frequency": null
                }
            ],
            "comprehensive_evaluation": {
                "risk": null,
                "interpretation": null,
                "metabolism_rate": null
            },
            "scientific_detail": []
        },
        "general_advice": null,
        "data_element_source_id": "610600",
        "data_element_source_domain": "omim",
        "result_interpretation": [],
        "references": {
            "articles": [],
            "knowledge": null,
            "authoritative_guide": null
        }
    }
}

......

```


## data_item_change_list

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/data-item/changelist)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `namespace` —— 命名空间;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `biosample_id` —— 生物样品编号;
* `from_batch_no` —— 批次号，默认为抽取过的最新的批次号（返回数据包含此批次）;
* `to_batch_no` —— 批次号，默认为抽取过的最新的批次号（返回数据包含此批次）；
* `next_page_key` —— 下一页参数，返回的数据中 next_page_key 不为空时，代表还有下一页数据；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.data_item_change_list(namespace='BGE', biosample_id='E-U19586714190', from_batch_no=1564650194901)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "biosample_id": "E-U19586714190",
    "data_element_ids": [],
    "next_page_key": null,
    "to_batch_no": null,
    "from_batch_no": 1564650194901,
    "batch_trace": {
        "prev_batch_no": null,
        "next_batch_no": null,
        "first_batch_no": null,
        "last_batch_no": null
    }
}
```
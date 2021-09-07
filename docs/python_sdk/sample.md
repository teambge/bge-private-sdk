## get_samples

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/sample/list)


![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `biosample_id` —— 生物样品编号；多个以英文逗号分割；
* `external_sample_id` —— 当前页码，默认 1；
* `page` —— 是否包含数据生成时间，可选值：surname、nation，多个用逗号分割；
* `limit` —— 一页最大返回数据量，默认 50；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
samples = private.get_samples(biosample_id='E-B19137107158,E-F19955300137,E-B19692615052')
for item in samples['result']:
    print(item.dumps(indent=4))
```

![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "external_sample_id": {
        "sample_id": "107201702599",
        "sample_id_alt": ""
    },
    "biosample_id": "E-B19137107158",
    "library": {
        "library_id": "",
        "library_strategy": null,
        "library_source": null,
        "library_selection": null,
        "library_layout": null,
        "insert_size": null,
        "nominal_size": null,
        "dnb_id": null
    },
    "sequencing": {
        "platform": null,
        "instrument_model": null,
        "instrument_serial_number": null,
        "read_type": null,
        "slide_id": null,
        "lane_id": null,
        "barcode": null,
        "sequencing_time": null,
        "raw_data_readnum": null,
        "raw_data_basenum": null,
        "raw_data_gc_content": null,
        "raw_data_n_count": null,
        "raw_data_q20": null,
        "raw_data_q30": null,
        "clean_data_readnum": null,
        "clean_data_basenum": null,
        "clean_data_gc_content": null,
        "clean_data_n_count": null,
        "clean_data_q20": null,
        "clean_data_q30": null,
        "fastq_backup_location": null
    },
    "statistics": {
        "coverage": null,
        "depth": null,
        "base_pairs": null,
        "variant_counting": null,
        "human_contamination": null
    },
    "alignment": {
        "mapping_rate": null,
        "pe_mapping_rate": null,
        "duplication_rate": null,
        "mismatch_rate": null,
        "chimerical_rate": null,
        "calculated_insert_size": null,
        "capture_rate_on_reads": null,
        "capture_rate_on_bases": null,
        "average_depth_rmdup": null,
        "coverage_gteq_1_fold": null,
        "coverage_gteq_2_fold": null,
        "coverage_gteq_3_fold": null,
        "coverage_gteq_4_fold": null,
        "coverage_gteq_5_fold": null,
        "coverage_gteq_10_fold": null,
        "coverage_gteq_20_fold": null,
        "coverage_gteq_30_fold": null,
        "coverage_gteq_100_fold": null,
        "uniformity_gt_point_2_fold": null
    },
    "budget_execution_unit_id": null,
    "status": -1,
    "l3_availability": false,
    "sample_time": null,
    "create_time": "2019-05-14T08:41:01Z",
    "update_time": "2020-08-24T06:31:52Z",
    "biosample_site": 10,
    "project": [
        {
            "project_id": "P-M19585209935",
            "project_name": "华小胖",
            "project_omic": "metagenomics",
            "public_description": "",
            "consortium": "华大基因",
            "data_provider": "国家基因库",
            "release_survey_id": null,
            "data_element": []
        }
    ]
}
{
    "external_sample_id": {
        "sample_id": "107201702598",
        "sample_id_alt": ""
    },
    "biosample_id": "E-F19955300137",
    "library": {
        "library_id": null,
        "library_strategy": null,
        "library_source": null,
        "library_selection": null,
        "library_layout": null,
        "insert_size": null,
        "nominal_size": null,
        "dnb_id": null
    },
    "sequencing": {
        "platform": null,
        "instrument_model": null,
        "instrument_serial_number": null,
        "read_type": null,
        "slide_id": null,
        "lane_id": null,
        "barcode": null,
        "sequencing_time": null,
        "raw_data_readnum": null,
        "raw_data_basenum": null,
        "raw_data_gc_content": null,
        "raw_data_n_count": null,
        "raw_data_q20": null,
        "raw_data_q30": null,
        "clean_data_readnum": null,
        "clean_data_basenum": null,
        "clean_data_gc_content": null,
        "clean_data_n_count": null,
        "clean_data_q20": null,
        "clean_data_q30": null,
        "fastq_backup_location": null
    },
    "statistics": {
        "coverage": null,
        "depth": null,
        "base_pairs": null,
        "variant_counting": null,
        "human_contamination": null
    },
    "alignment": {
        "mapping_rate": null,
        "pe_mapping_rate": null,
        "duplication_rate": null,
        "mismatch_rate": null,
        "chimerical_rate": null,
        "calculated_insert_size": null,
        "capture_rate_on_reads": null,
        "capture_rate_on_bases": null,
        "average_depth_rmdup": null,
        "coverage_gteq_1_fold": null,
        "coverage_gteq_2_fold": null,
        "coverage_gteq_3_fold": null,
        "coverage_gteq_4_fold": null,
        "coverage_gteq_5_fold": null,
        "coverage_gteq_10_fold": null,
        "coverage_gteq_20_fold": null,
        "coverage_gteq_30_fold": null,
        "coverage_gteq_100_fold": null,
        "uniformity_gt_point_2_fold": null
    },
    "budget_execution_unit_id": null,
    "status": -1,
    "l3_availability": false,
    "sample_time": null,
    "create_time": "2019-05-14T08:41:01Z",
    "update_time": "2020-08-24T06:31:52Z",
    "biosample_site": 10,
    "project": [
        {
            "project_id": "P-M19585209935",
            "project_name": "华小胖",
            "project_omic": "metagenomics",
            "public_description": "",
            "consortium": "华大基因",
            "data_provider": "国家基因库",
            "release_survey_id": null,
            "data_element": []
        }
    ]
}
```

## register_sample

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/sample/register)

![args](https://img.shields.io/badge/请求参数-args-blue)

* `biosample_site` —— 采样部位，取值范围：1-14;
* `project_id` —— 项目编号;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `external_sample_id` —— 外部生物样品 id;

**更多参数参考**：[采样位置](https://api.private.omgut.com/doc/#/appendix/readme?id=%E9%87%87%E6%A0%B7%E4%BD%8D%E7%BD%AE)


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=60, verbose=False)
register = private.register_sample(biosample_site=11, project_id='P-W19770800157', external_sample_id='S0ad004', depth=46.612)
print(register.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "biosample_id": "E-U19342736148"
}
```


## improve_sample

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/sample/improve)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `biosample_id` —— 生物样品编号;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

**更多参数参考**：[补充数据](https://api.private.omgut.com/doc/#/sample/improve?id=%E6%B5%8B%E5%BA%8F)

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=60, verbose=False)
result = private.improve_sample(biosample_id='E-B19137107158', depth=1)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "biosample_id": "E-B19137107158",
    "depth": 1
}
```







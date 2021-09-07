## get_taxon_abundance

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/abundance/taxon)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `biosample_id` —— 生物样品编号;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `page	` —— 当前页码，默认 1;
* `limit` —— 一页最大返回数据量，默认 50;
* `sort_by` —— 排序字段；
* `sort_direction` —— 排序方向；
* `taxon_id` —— BGE 物种编号(以NCBI txid为准), 由 txid + 数字id两部分组成, 多个物种编号以逗号 , 分割，如: txid165179,txid239934; 


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.get_taxon_abundance(biosample_id='E-S19848860371', limit=2)
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "sample_info": {
        "biosample_site": "saliva",
        "biosample_id": "E-S19848860371",
        "sample_time": "2018-09-02T16:00:00+0000"
    },
    "platform_labels": null,
    "background": {
        "mean": 0.540127553191489,
        "freq": 1.0,
        "reference_cohort": "Chinese Adult",
        "rank_ratio": ">=11%",
        "background": {
            "100%": 3.04703,
            "5%": 0.074684,
            "75%": 0.738015,
            "95%": 1.6802695,
            "0%": 0.03687,
            "50%": 0.349775,
            "25%": 0.1570575
        }
    },
    "observation": {
        "type": "relative abundance",
        "unit": "percent",
        "value": 0.09427
    },
    "taxonomy": {
        "taxon_name": "s__Veillonella_parvula",
        "taxon_id": "txid29466",
        "coding": {
            "system": "https://www.ncbi.nlm.nih.gov/Taxonomy"
        },
        "lineage": "k__Bacteria|p__Firmicutes|c__Negativicutes|o__Selenomonadales|f__Veillonellaceae|g__Veillonella|s__Veillonella_parvula",
        "rank": "species"
    }
}
{
    "sample_info": {
        "biosample_site": "saliva",
        "biosample_id": "E-S19848860371",
        "sample_time": "2018-09-02T16:00:00+0000"
    },
    "platform_labels": null,
    "background": {
        "mean": 0.397395744680851,
        "freq": 0.840425531914894,
        "reference_cohort": "Chinese Adult",
        "rank_ratio": ">=31%",
        "background": {
            "100%": 2.85998,
            "5%": 0.0,
            "75%": 0.37865,
            "95%": 1.9271885,
            "0%": 0.0,
            "50%": 0.10055,
            "25%": 0.012935
        }
    },
    "observation": {
        "type": "relative abundance",
        "unit": "percent",
        "value": 0.02583
    },
    "taxonomy": {
        "taxon_name": "s__Megasphaera_micronuciformis",
        "taxon_id": "txid187326",
        "coding": {
            "system": "https://www.ncbi.nlm.nih.gov/Taxonomy"
        },
        "lineage": "k__Bacteria|p__Firmicutes|c__Negativicutes|o__Selenomonadales|f__Veillonellaceae|g__Megasphaera|s__Megasphaera_micronuciformis",
        "rank": "species"
    }
}
```


## get_func_abundance

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/abundance/func)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `biosample_id` —— 生物样品编号;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `next_page` —— 下一页参数，用于获取下一页数据；
* `limit` —— 一页最大返回数据量，默认 50;
* `ids` —— BGE 物种功能编号，多个值以逗号 , 分割，如：BT1,BT2；

**注意**： ids 与 limit、next_page 参数互斥，如果出现 limit 或 next_page，则不能出现参数 ids；反之亦然

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.get_func_abundance(biosample_id='E-F19486142636', catalog='go')
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
"coding": {
    "id": "GO:0002084",
    "system": "go_HUMAnN2_0.11"
},
"observation": {
    "value": 1.86433e-06,
    "unit": "percent",
    "type": "relative abundance"
},
"sample_info": {
    "sample_time": null,
    "biosample_site": "feces",
    "biosample_id": "E-F19956815350"
},
"data_element_id": "f4a406cf-b363-11e9-bfed-00163e104c79",
"platform_labels": []
},
{
    "coding": {
        "id": "GO:0002097",
        "system": "go_HUMAnN2_0.11"
    },
    "observation": {
        "value": 4.23543e-07,
        "unit": "percent",
        "type": "relative abundance"
    },
    "sample_info": {
        "sample_time": null,
        "biosample_site": "feces",
        "biosample_id": "E-F19956815350"
    },
    "data_element_id": "f4a406dc-b363-11e9-bfed-00163e104c79",
    "platform_labels": []
},
{
    "coding": {
        "id": "GO:0002098",
        "system": "go_HUMAnN2_0.11"
    },
    "observation": {
        "value": 7.97779e-05,
        "unit": "percent",
        "type": "relative abundance"
    },
    "sample_info": {
        "sample_time": null,
        "biosample_site": "feces",
        "biosample_id": "E-F19956815350"
    },
    "data_element_id": "f4a406dd-b363-11e9-bfed-00163e104c79",
    "platform_labels": []
},
{
    "coding": {
        "id": "GO:0002100",
        "system": "go_HUMAnN2_0.11"
    },
    "observation": {
        "value": 0.000101617,
        "unit": "percent",
        "type": "relative abundance"
    },
    "sample_info": {
        "sample_time": null,
        "biosample_site": "feces",
        "biosample_id": "E-F19956815350"
    },
    "data_element_id": "f4a406df-b363-11e9-bfed-00163e104c79",
    "platform_labels": []
},
{
    "coding": {
        "id": "GO:0002101",
        "system": "go_HUMAnN2_0.11"
    },
    "observation": {
        "value": 7.954e-07,
        "unit": "percent",
        "type": "relative abundance"
    },
    "sample_info": {
        "sample_time": null,
        "biosample_site": "feces",
        "biosample_id": "E-F19956815350"
    },
    "data_element_id": "f4a406e0-b363-11e9-bfed-00163e104c79",
    "platform_labels": []
}
```


## get_gene_abundance

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/abundance/gene)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `biosample_id` —— 生物样品编号;
* `catalog` —— 分类标签；可选值：IGC_9.9M、UniRef90_HUMAnN2_0.11;
* `data_type` —— 返回数据类型；可选值：list、file;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `ids	` —— BGE 物种 IGC 基因编号，多个值以逗号 , 分割，如：igc_50,igc_51;
* `limit` —— 一页最大返回数据量，默认 50;
* `next_page` —— 接口返回的下一页参数；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.get_gene_abundance(biosample_id='E-F19486142636', catalog='IGC_9.9M', data_type='list' ,limit=2)  # 线上环境
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "sample_info": {
        "biosample_id": "E-F19486142636",
        "biosample_site": "feces",
        "sample_time": "2018-08-15T16:00:00+0000"
    },
    "platform_labels": null,
    "igc_gene": {
        "igc_gene_id": "igc_1",
        "annotation": {
            "phylum": "unknown",
            "genus": "unknown",
            "gene_completeness": "Complete",
            "gene_length": 88230,
            "kegg_annotation": "K01824",
            "eggnog_annotation": "COG5184"
        },
        "igc_gene_name": "T2D-6A_GL0083352",
        "coding": {
            "system": "http://meta.genomics.cn"
        }
    },
    "observation": {
        "type": "relative abundance",
        "value": 3.46157389540114e-09,
        "unit": "percent",
        "software": "IGC_PROFILING(10.1038/nbt.2942/)"
    }
}
{
    "sample_info": {
        "biosample_id": "E-F19486142636",
        "biosample_site": "feces",
        "sample_time": "2018-08-15T16:00:00+0000"
    },
    "platform_labels": null,
    "igc_gene": {
        "igc_gene_id": "igc_2",
        "annotation": {
            "phylum": "unknown",
            "genus": "unknown",
            "gene_completeness": "Complete",
            "gene_length": 88086,
            "kegg_annotation": "K01824",
            "eggnog_annotation": "COG5184"
        },
        "igc_gene_name": "V1.UC4-5_GL0154511",
        "coding": {
            "system": "http://meta.genomics.cn"
        }
    },
    "observation": {
        "type": "relative abundance",
        "value": 2.11093288550184e-07,
        "unit": "percent",
        "software": "IGC_PROFILING(10.1038/nbt.2942/)"
    }
}
```
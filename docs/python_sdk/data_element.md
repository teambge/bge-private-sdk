## data_element_search

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/search)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `query` —— 查询文本;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `data_element_source_domains` —— 数据元 source_domain，逗号分割多个 source_domain；该字段只在 types 为空，或 types 包含 data_element 时提供;
* `limit` —— 每页返回数量;
* `page` —— 当前页；
* `types` —— 搜索的数据类型，取值范围：data_element、collection、data_element,collection，不提供参数时默认搜索两种数据类型；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.data_element_search('MF50.60,dede')
for item in result['result']:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "id": "9622a9d4-b8ec-11e9-bfed-00163e104c79",
    "data": {
        "icd10_name_en": "Other difficulties with micturition",
        "data_element_description": "",
        "data_element_name": "排尿踌躇",
        "type": "data_element",
        "data_element_name_en": "Hesitancy of micturition",
        "data_element_source_domain": "icd_11",
        "flag": 1,
        "category": "症状、体征或临床所见，不可归类在他处者",
        "effected_flag": "1",
        "data_element_source_id": "MF50.60",
        "uri": "http://id.who.int/icd/entity/1323766251",
        "data_element_id": "9622a9d4-b8ec-11e9-bfed-00163e104c79",
        "icd10_code": "R39.1"
    },
    "type": "data_element",
    "highlight": {
        "data_element_source_id": "<span class=\"highlight\">MF50.60</span>"
    },
    "app": "bge_v2"
}
```

## get_data_element

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/data-element-byid)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `data_element_id` —— 数据元编号;


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.get_data_element('00011d12-b363-11e9-bfed-00163e104c79')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "alt": [
        {
            "type": "SNV",
            "sequence": "A"
        }
    ],
    "data_element_source_domain": "human_9606_b151_GRCh38p7",
    "data_element_source_id": "rs1421970240",
    "info": {
        "WGT": 1,
        "VP": "0x0500000a0005000002000100",
        "ASP": true,
        "RS": 1421970240,
        "RSPOS": 1420044,
        "GENEINFO": "LOC105378585:105378585|ANKRD65:441869",
        "R5": true,
        "TOPMED": [
            "0.99999203618756371",
            "0.00000796381243628"
        ],
        "VC": "SNV",
        "SSR": 0,
        "SAO": 0,
        "dbSNPBuildID": 151,
        "INT": true
    },
    "db_snp_build_id": 151,
    "chr_pos": "1:1420044",
    "data_element_id": "00011d12-b363-11e9-bfed-00163e104c79",
    "type": "snp",
    "ref": "G"
}
```

## data_element_by_source

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/data-element-bysource)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `data_element_source_domain` —— 数据元来源域;
* `data_element_source_id` —— 数据元来源编号;


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.data_element_by_source('human_9606_b151_GRCh38p7', 'rs1421970240')
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "chr_pos": "1:1420044",
    "db_snp_build_id": 151,
    "data_element_source_domain": "human_9606_b151_GRCh38p7",
    "data_element_id": "00011d12-b363-11e9-bfed-00163e104c79",
    "ref": "G",
    "alt": [
        {
            "type": "SNV",
            "sequence": "A"
        }
    ],
    "type": "snp",
    "info": {
        "RSPOS": 1420044,
        "ASP": true,
        "R5": true,
        "SSR": 0,
        "VP": "0x0500000a0005000002000100",
        "WGT": 1,
        "SAO": 0,
        "GENEINFO": "LOC105378585:105378585|ANKRD65:441869",
        "VC": "SNV",
        "RS": 1421970240,
        "INT": true,
        "TOPMED": [
            "0.99999203618756371",
            "0.00000796381243628"
        ],
        "dbSNPBuildID": 151
    },
    "data_element_source_id": "rs1421970240"
}
```


## batch_data_element_by_source

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/data-element-batch-bysource)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `data_element_source_domain` —— 数据元来源域;
* `data_element_source_ids` —— 数据元来源编号，逗号分隔多个;


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.batch_data_element_by_source('human_9606_b151_GRCh38p7', 'rs1421970240,rs1421970241')
for item in result['result']:
    print(item.json())
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "data_element_id": "7533bda0-a3d7-11ea-bbbd-48a47299ee4a",
    "alt": [
        {
            "type": "SNV",
            "sequence": "C"
        }
    ],
    "chr_pos": "5:68204836",
    "data_element_source_domain": "test_domain",
    "data_element_source_id": "rs188276406",
    "db_snp_build_id": 135,
    "info": {
        "ASP": true,
        "COMMON": 1,
        "SSR": 0,
        "SAO": 0,
        "VC": "SNV",
        "KGPhase3": true,
        "dbSNPBuildID": 135,
        "TOPMED": [
            "0.99882135575942915",
            "0.00117864424057084"
        ],
        "WGT": 1,
        "VLD": true,
        "RS": 188276406,
        "CAF": [
            "0.998",
            "0.001997"
        ],
        "KGPhase1": true,
        "VP": "0x050000000005040036000100",
        "RSPOS": 68204836
    },
    "ref": "T",
    "type": "snp"
},
{
    "data_element_id": "52808b24-a177-11ea-a6ff-48a47299ee4a",
    "alt": [
        {
            "type": "SNV",
            "sequence": "C"
        }
    ],
    "annotation": {
        "GeneDamage_all": [
            0,
            "__*__"
        ],
        "gnomAD_genomes_AF": [
            0,
            "__*__"
        ],
        "HGVS_IVS": [
            "c.IVS1+28689T>C",
            "__*__"
        ],
        "NativeInterp": [
            0,
            "__*__"
        ],
        "Interactions_BioGRID": [
            [
                "IQCB1"
            ],
            "__*__"
        ],
        "G1000_AMR_AF": [
            0,
            "__*__"
        ],
        "Depth": [
            38,
            "__*__"
        ],
        "dbscSNV_ADA_SCORE": [
            "n.569+28689T>C",
            "__*__"
        ],
        "Gene_MIM_id": [
            600755,
            "__*__"
        ],
        "TumorHeartFreq_Het": [
            0,
            "__*__"
        ],
        "GENE": [
            "SYN2",
            "__*__"
        ],
        "CODON": [
            478,
            582
        ],
        "gnomad_exomes_AF_EAS": [
            0,
            "__*__"
        ],
        "Pathway_KEGG_full": [
            "SYN2",
            "__*__"
        ],
        "EntrezGeneID": [
            "ENSG00000157152",
            "__*__"
        ],
        "Zygosity": [
            "hom-alt",
            "__*__"
        ],
        "EFFECT": [
            "Intron",
            "__*__"
        ],
        "gatkQUAL": [
            1324,
            "__*__"
        ],
        "gene_family_id": [
            "Synapsins",
            "__*__"
        ],
        "NPID": [
            "ACCACTTATT.CAGAACATCT",
            "__*__"
        ],
        "Exon_mutname": [
            1,
            "__*__"
        ],
        "EnsemblGeneID": [
            1325,
            "__*__"
        ],
        "gnomad_exomes_AF_AMR": [
            0,
            "__*__"
        ],
        "Phenotypes": [
            "{Schizophrenia, susceptibility to}, 181500 (3), Autosomal dominant. 181500(SK)",
            "__*__"
        ],
        "Alias": [
            6854,
            "__*__"
        ],
        "P_HI": [
            [
                "YWHAE",
                "IQCB1",
                "DNAAF2",
                "SYN3",
                "SYN2",
                "YWHAZ",
                "SYN1",
                "GNB2L1",
                "ARMC1",
                "DGUOK",
                "HAX1",
                "PSMC3",
                "NOS1AP",
                "POLL"
            ],
            "__*__"
        ],
        "G1000_AF": [
            0,
            "__*__"
        ],
        "A.Ratio": [
            1,
            "__*__"
        ],
        "NativeFreq_Hom": [
            0,
            "__*__"
        ],
        "GO_molecular_function": [
            [
                "chemical synaptic transmission",
                "neurotransmitter secretion"
            ],
            "__*__"
        ],
        "TRID": [
            "NM_003178",
            "NM_133625"
        ],
        "dbSNP_AF": [
            0,
            "__*__"
        ],
        "TumorHeartFreq_Hom": [
            0,
            "__*__"
        ],
        "Possible_Inheritance": [
            "AD",
            "__*__"
        ],
        "G1000_EAS_AF": [
            0,
            "__*__"
        ],
        "Strand": [
            "+",
            "__*__"
        ],
        "ESP6500_MAF": [
            0,
            "__*__"
        ],
        "EXAC_AF": [
            0,
            "__*__"
        ],
        "gnomad_exomes_AF": [
            0,
            "__*__"
        ],
        "HGVS_C": [
            "c.377+28689T>C",
            "__*__"
        ],
        "Expression_egenetics": [
            [
                "catalytic activity",
                "ATP binding"
            ],
            "__*__"
        ],
        "FLKSEQ": [
            "p25.2",
            "__*__"
        ],
        "NbGID": [
            0,
            "__*__"
        ]
    },
    "chr_pos": "3:12033617",
    "data_element_source_domain": "test_domain",
    "data_element_source_id": "rs394945",
    "db_snp_build_id": 80,
    "info": {
        "dbSNPBuildID": 80,
        "RS": 394945,
        "SSR": 0,
        "COMMON": 1,
        "TOPMED": [
            "0.10883346075433231",
            "0.89116653924566768"
        ],
        "ASP": true,
        "CAF": [
            "0.07268",
            "0.9273"
        ],
        "SLO": true,
        "G5": true,
        "INT": true,
        "VLD": true,
        "KGPhase1": true,
        "SAO": 0,
        "KGPhase3": true,
        "GENEINFO": "SYN2:6854",
        "VC": "SNV",
        "RSPOS": 12033617,
        "VP": "0x05010008000515013e000100",
        "WGT": 1,
        "GNO": true
    },
    "ref": "T",
    "type": "snp"
}
```


## replace_data_element

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/replace)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `data_element_source_domain` —— 数据元来源域;
* `data_element_source_id` —— 数据元来源编号;
* `columns` —— 需要更新或创建的数据元属性；JSON 格式字符串；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
columns = {
    "db_snp_build_id": 83,
    "annotation": {
        "Exon_mutname": [
            -1
        ],
        "Zygosity": [
            "hom-alt"
        ],
        "FLKSEQ": [
            "q22.3"
        ],
        "G1000_EAS_AF": [
            0
        ],
        "dbSNP_AF": [
            0
        ],
        "gatkQUAL": [
            2071
        ],
        "gnomad_exomes_AF_AMR": [
            0
        ],
        "gnomad_exomes_AF_EAS": [
            0
        ],
        "PMC": [
            1
        ],
        "CODON": [
            -1
        ],
        "NbGID": [
            0
        ],
        "NativeInterp": [
            0
        ],
        "NPID": [
            "TAGTGAGCAA.GTAAACATGA"
        ],
        "Depth": [
            56
        ],
        "GWAS_traitNativeFreq_Het": [
            "Rheumatoid arthritis"
        ],
        "HGVS_IVS": [
            "c.101451374G>A"
        ],
        "EXAC_AF": [
            0
        ],
        "gnomad_exomes_AF": [
            0
        ],
        "G1000_AMR_AF": [
            0
        ],
        "TumorHeartFreq_Hom": [
            0
        ],
        "TumorHeartFreq_Het": [
            0
        ],
        "gnomAD_genomes_AF": [
            0
        ],
        "G1000_AF": [
            0
        ],
        "GENE": [
            "NACAP1-GRHL2"
        ],
        "HGVS_C": [
            "n.101451374G>A"
        ],
        "ESP6500_MAF": [
            0
        ],
        "PM": [
            1
        ],
        "dbscSNV_ADA_SCORE": [
            "n.101451374G>A"
        ],
        "EFFECT": [
            "Intergenic"
        ],
        "A.Ratio": [
            1
        ],
        "NativeFreq_Hom": [
            0
        ]
    },
    "type": "snp",
    "ref": "G",
    "alt": [
        {
            "type": "SNV",
            "sequence": "A"
        },
        {
            "type": "SNV",
            "sequence": "C"
        }
    ],
    "info": {
        "COMMON": 1,
        "VC": "SNV",
        "SSR": 0,
        "RV": True,
        "TOPMED": [
            "0.35196865443425076",
            "0.64791985219164118",
            "0.00011149337410805"
        ],
        "GNO": True,
        "RS": 678347,
        "VLD": True,
        "KGPhase3": True,
        "SAO": 0,
        "KGPhase1": True,
        "G5A": True,
        "CAF": [
            "0.4473",
            "0.5527",
            True
        ],
        "HD": True,
        "G5": True,
        "WGT": 1,
        "dbSNPBuildID": 83,
        "VP": "0x05012000000517053e020100",
        "RSPOS": 101451374,
        "PM": True,
        "MTP": True,
        "ASP": True,
        "SLO": True
    },
    "chr_pos": "8:101451374"
}
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.replace_data_element('test_domain_s', 'rs678347', columns)
print(result.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "chr_pos": "8:101451374",
    "annotation": {
        "NativeInterp": [
            0
        ],
        "TumorHeartFreq_Hom": [
            0
        ],
        "Exon_mutname": [
            -1
        ],
        "HGVS_IVS": [
            "c.101451374G>A"
        ],
        "gnomad_exomes_AF": [
            0
        ],
        "A.Ratio": [
            1
        ],
        "gnomad_exomes_AF_AMR": [
            0
        ],
        "gnomad_exomes_AF_EAS": [
            0
        ],
        "G1000_AF": [
            0
        ],
        "FLKSEQ": [
            "q22.3"
        ],
        "Zygosity": [
            "hom-alt"
        ],
        "NativeFreq_Hom": [
            0
        ],
        "gatkQUAL": [
            2071
        ],
        "dbscSNV_ADA_SCORE": [
            "n.101451374G>A"
        ],
        "CODON": [
            -1
        ],
        "NbGID": [
            0
        ],
        "gnomAD_genomes_AF": [
            0
        ],
        "NPID": [
            "TAGTGAGCAA.GTAAACATGA"
        ],
        "ESP6500_MAF": [
            0
        ],
        "G1000_EAS_AF": [
            0
        ],
        "HGVS_C": [
            "n.101451374G>A"
        ],
        "TumorHeartFreq_Het": [
            0
        ],
        "PMC": [
            1
        ],
        "EFFECT": [
            "Intergenic"
        ],
        "GENE": [
            "NACAP1-GRHL2"
        ],
        "EXAC_AF": [
            0
        ],
        "G1000_AMR_AF": [
            0
        ],
        "Depth": [
            56
        ],
        "PM": [
            1
        ],
        "dbSNP_AF": [
            0
        ],
        "GWAS_traitNativeFreq_Het": [
            "Rheumatoid arthritis"
        ]
    },
    "db_snp_build_id": 83,
    "type": "snp",
    "alt": [
        {
            "sequence": "A",
            "type": "SNV"
        },
        {
            "sequence": "C",
            "type": "SNV"
        }
    ],
    "data_element_source_domain": "test_domain_s",
    "flag": 1,
    "info": {
        "RV": true,
        "ASP": true,
        "SLO": true,
        "G5": true,
        "CAF": [
            "0.4473",
            "0.5527",
            true
        ],
        "SAO": 0,
        "dbSNPBuildID": 83,
        "COMMON": 1,
        "G5A": true,
        "TOPMED": [
            "0.35196865443425076",
            "0.64791985219164118",
            "0.00011149337410805"
        ],
        "WGT": 1,
        "KGPhase3": true,
        "VP": "0x05012000000517053e020100",
        "RS": 678347,
        "RSPOS": 101451374,
        "MTP": true,
        "HD": true,
        "VC": "SNV",
        "SSR": 0,
        "KGPhase1": true,
        "VLD": true,
        "GNO": true,
        "PM": true
    },
    "data_element_source_id": "rs678347",
    "data_element_id": "bde02390-0c90-11ec-9d30-00163e0c480e",
    "ref": "G"
}
```


## merge_data_element

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/merge)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `data_element_ids` —— 被合并的数据元编号，逗号分割多个；
* `merge_data_element_id` —— 合并到的数据元编号；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `comment` —— 备注；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
private.merge_data_element('test_domain_s', 'rs678347', comment='增加备注')
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
```


## discard_data_element

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/data-element/discard)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `data_element_source_domain` —— 数据元来源域;
* `data_element_source_id` —— 数据元来源编号;


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=16, verbose=False)
result = private.discard_data_element('xj_test_domain', 'rs678347')
print(result)
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
Model({'data_element_id': '5662d06e-0afb-11ec-a5b1-c8b29b0eab1e'})
```
## genome_variant

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/variant/v2)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `biosample_id` —— 生物样品编号;
* `rsids` —— rsid；多个 rsid 通过逗号分割;

![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=60, verbose=False)
result = private.genome_variant(biosample_id='E-B19593615052', rsids='rs14,rs133,rs324,rs546')
for item in result:
    print(item.dumps(indent=4))
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "coordinate_system": 0, 
    "variant": {
        "information": {
            "site_quality": 130.23, 
            "frequency": {
                "CAF": [
                    0.998, 
                    0.001997
                ], 
                "TOPMED": [
                    0.9967029816513762, 
                    0.00329701834862385
                ]
            }, 
            "DP": 37, 
            "AN": 2
        }, 
        "genotype": "T/T", 
        "reference_base": "T", 
        "type": "snp", 
        "call": {
            "RGQ": 102, 
            "GT": "0/0", 
            "AD": [
                37, 
                0
            ], 
            "DP": 37
        }, 
        "position": 19960584, 
        "alternate_base": [
            "C"
        ], 
        "chromosome": "chr8"
    }, 
    "genomic_context": {
        "gene": [
            {
                "symbol": "LPL", 
                "version": {
                    "Genomic": [], 
                    "RNA": [], 
                    "mRNA_and_protein": [
                        {
                            "protein": null, 
                            "mRNA": "NM_000237"
                        }
                    ]
                }, 
                "coding": {
                    "system": "https://www.ncbi.nlm.nih.gov"
                }
            }
        ]
    }, 
    "alternate_id": [
        "rs315"
    ], 
    "is_no_call": false, 
    "source": {
        "update_time": 1566890658239, 
        "tag": {
            "dbSNP_build": 151, 
            "assembly_synonym": "GRCh38"
        }, 
        "pipeline_version": "WGSAI3.0-l"
    }, 
    "is_genotyped": true, 
    "variant_id": "52fee8a0-b53b-11e9-bfed-00163e104c79", 
    "is_assayed": true
}, 
{
    "coordinate_system": 0, 
    "variant": {
        "information": {
            "site_quality": 127.23, 
            "frequency": {
                "CAF": [], 
                "TOPMED": []
            }, 
            "DP": 38, 
            "AN": 2
        }, 
        "genotype": "T/T", 
        "reference_base": "T", 
        "type": "snp", 
        "call": {
            "RGQ": 99, 
            "GT": "0/0", 
            "AD": [
                38, 
                0
            ], 
            "DP": 38
        }, 
        "position": 27916460, 
        "alternate_base": [
            "C"
        ], 
        "chromosome": "chr7"
    }, 
    "genomic_context": {
        "gene": [
            {
                "symbol": "JAZF1", 
                "version": {
                    "Genomic": [], 
                    "RNA": [], 
                    "mRNA_and_protein": [
                        {
                            "protein": null, 
                            "mRNA": "NM_175061"
                        }
                    ]
                }, 
                "coding": {
                    "system": "https://www.ncbi.nlm.nih.gov"
                }
            }
        ]
    }, 
    "alternate_id": [
        "rs219"
    ], 
    "is_no_call": false, 
    "source": {
        "update_time": 1566888780453, 
        "tag": {
            "dbSNP_build": 151, 
            "assembly_synonym": "GRCh38"
        }, 
        "pipeline_version": "WGSAI3.0-l"
    }, 
    "is_genotyped": true, 
    "variant_id": "88e29db9-b503-11e9-bfed-00163e104c79", 
    "is_assayed": true
}
```


## professional_variant

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/variant/professional-variant)


![args](https://img.shields.io/badge/请求参数-args-blue)

* `biosample_id` —— 生物样品编号;
* `only_variant_site` —— 是否仅输出变异位置；默认为 True;
* `biosample_id` —— 生物样品编号;
* `biosample_id` —— 生物样品编号;

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `regions	` —— 需要抽取区域的坐标数组，数组长度不得超过5000；例：[{"chrom": "chr1","begin": 1013977,"end": 1013978}];
* `biosample_id` —— 需要抽取区域的BED文件，文件须为 zip 压缩文件且内容不得超过100w行;

**注意**： 参数 regions 与 bed_file 互斥，每次请求只允许提供其中之一


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=60, verbose=False)
result = private.professional_variant(biosample_id='E-B19137107158', only_variant_site=False, regions='[{"chr": "chr3","begin": 21733,"end": 30691},{"chr": "chr1","begin": 629556,"end": 784860},{"chr": "chr1","begin": 784860,"end": 817186}]')
或者
bed_file = open('/home/xiangji/Desktop/bed_file测试文件/full.all.3.bed.zip', 'rb')
result = private.professional_variant(biosample_id='E-B19137107158', only_variant_site=False, bed_file='/home/xiangji/Desktop/bed_file测试文件/full.all.3.bed.zip')

print(result)
```


![Success](https://img.shields.io/badge/Output-Success-green)

```json
Model({'task_id': '44e5b0fc-699c-4350-8b60-4f66f1618920'})
```
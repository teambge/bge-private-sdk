## get_user

[![私有平台接口文档](https://img.shields.io/badge/私有平台接口文档-lightgrey)](https://api.private.omgut.com/doc/#/user/readme)

获取用户编号（非用户中心用户 ID）、出生日期、性别、籍贯、星座、姓氏、民族；

![kwargs](https://img.shields.io/badge/请求参数-kwargs-blue)

* `biosample_id` —— 生物样品编号，获取此样品所属用户的个人信息；
* `fundamental_entity_id` —— 个体编号，获取当前个体的用户个人信息；
* `has_generate_time_fields` —— 是否包含数据生成时间，可选值：surname、nation，多个用逗号分割；

**注意**：biosample_id 和 fundamental_entity_id 必须且仅支持提供其中之一；


![Python 示例](https://img.shields.io/badge/示例-Python-lightgrey)

```python
private = PrivateAPI(app_key, app_secret, endpoint=endpoint,
                 max_retries=3, timeout=60, verbose=False)
user = private.get_user(biosample_id='E-B19137107158')
print(user.dumps(indent=4))
```

![Success](https://img.shields.io/badge/Output-Success-green)

```json
{
    "fundamental_entity_id": "594e5bc0-a1bc-11eb-b664-c8b29b0eab1e",
    "birthday": "2010-11-11",
    "gender": 1,
    "native_place": {},
    "constellation": "天蝎座",
    "nation": "",
    "surname": ""
}
```


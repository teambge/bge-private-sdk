# -*- coding: utf-8 -*-

import json

from six.moves import UserDict
from weakref import proxy


class Model(UserDict):
    """统一的接口返回数据包装模型类

    所有接口的返回值都使用本类进行封装。

    使用示例:

        >>> print(Model({}))
        Model({})
        >>> inst = Model({})
        >>> inst['demo'] = 1
        >>> print(inst.demo)
        1
        >>> print(inst['demo'])
        1
        >>> demo = {
            'x': [{
                'x1': 'x1'
            }],
            'y': {
                'y1': 'y1'
            }
        }
        >>> m = Model(demo)
        >>> print(m)
        Model({'y': Model({'y1': 'y1'}), 'x': [Model({'x1': 'x1'})]})
        >>> j = m.json()
        >>> print(type(j))
        <type 'dict'>
        >>> print(j)
        {'y': {'y1': 'y1'}, 'x': [{'x1': 'x1'}]}
        >>> s = m.dumps(indent=4)
        >>> print(type(s))
        <type 'str'>
        >>> print(s)
        {
            "y": {
                "y1": "y1"
            }, 
            "x": [
                {
                    "x1": "x1"
                }
            ]
        }
    """

    def __init__(self, data):
        ret = {}
        for key, val in data.items():
            ret[key] = self._encode_data(val)
        UserDict.__init__(self, ret)

    def __getattr__(self, name):
        try:
            return self.data[name]
        except KeyError:
            raise AttributeError(name)

    def json(self):
        """返回可 JSON 序列化的对象"""
        ret = {}
        for key, value in self.data.items():
            ret[key] = self._decode_data(value)
        return ret

    def dumps(self, indent=None, ensure_ascii=None, **kwargs):
        r = self.json()
        return json.dumps(
            r, indent=indent, ensure_ascii=ensure_ascii, **kwargs)

    def _encode_data(self, val):
        if isinstance(val, dict):
            ret = {}
            for sub_key, sub_val in val.items():
                ret[sub_key] = self._encode_data(sub_val)
            return self.__class__(ret)
        elif isinstance(val, list):
            ret = []
            for sub_val in val:
                ret.append(self._encode_data(sub_val))
            return ret
        else:
            return val

    def _decode_data(self, val):
        if isinstance(val, Model):
            ret = {}
            for sub_key, sub_val in val.items():
                ret[sub_key] = self._decode_data(sub_val)
            return ret
        elif isinstance(val, list):
            ret = []
            for sub_val in val:
                ret.append(self._decode_data(sub_val))
            return ret
        else:
            return val

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self.data)

    def __repr__(self):
        return '<%s object at %s>' % (
            self.__class__.__name__, hex(id(self)))

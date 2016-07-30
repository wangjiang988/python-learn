#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# GET请求

# 1、无参数实例

import requests

ret = requests.get('https://github.com/timeline.json')

print(ret.url)
print(ret.text)



# 2、有参数实例

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.get("http://httpbin.org/get", params=payload)

print(ret.url)
print(ret.text)

# POST请求
# 1、基本POST实例

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.post("http://httpbin.org/post", data=payload)

print(ret.text)


# 2、发送请求头和数据实例

import requests
import json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

ret = requests.post(url, data=json.dumps(payload), headers=headers)

print(ret.text)
print(ret.cookies)

# 其它请求
"""
requests.get(url, params=None, **kwargs)
requests.post(url, data=None, json=None, **kwargs)
requests.put(url, data=None, **kwargs)
requests.head(url, **kwargs)
requests.delete(url, **kwargs)
requests.patch(url, data=None, **kwargs)
requests.options(url, **kwargs)

# 以上方法均是在此方法的基础上构建
requests.request(method, url, **kwargs)

更多requests模块相关的文档见：http://cn.python-requests.org/zh_CN/latest/

"""
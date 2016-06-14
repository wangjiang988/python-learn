#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import json

dic = {'k1': 'v1'}
print(dic, type(dic))

# 将python基本数据类型转化成字符串形式
result = json.dumps(dic)
print(result, type(result))


string = '{"Year": 2016}'
print(string, type(string))

# 将字符串形式转化成基本数据类型
str_inp = json.loads(string)
print(str_inp, type(str_inp))
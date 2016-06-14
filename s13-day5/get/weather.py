#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import requests
import json

response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
response.encoding = 'utf-8'

dic = json.loads(response.text)  # .text返回的内容
for key in dic:
    print(key, dic[key])


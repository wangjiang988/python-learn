#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 检测QQ账号是否在线

import urllib
import requests
from xml.etree import ElementTree as ET

# 使用内置模块urllib发送HTTP请求，或者XML格式内容
"""
f = urllib.request.urlopen('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=554248852')
result = f.read().decode('utf-8')
"""


# 使用第三方模块requests发送HTTP请求，或者XML格式内容
r = requests.get('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=365051764')
result = r.text

# 解析XML格式内容
node = ET.XML(result)

# 获取内容
if node.text == "Y":
    print("在线")
else:
    print("离线")

#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 发送GET请求
import urllib.request

f = urllib.request.urlopen(
    'http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=554248852')
result = f.read().decode('utf-8')

print(result)

# 发送携带请求头的GET请求
# import urllib.request

req = urllib.request.Request('http://www.example.com/')
req.add_header('Referer', 'http://www.python.org/')
r = urllib.request.urlopen(req)

result = r.read().decode('utf-8')

print(result)
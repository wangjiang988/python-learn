#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 基本加密
import hashlib

obj = hashlib.md5()
obj.update(bytes('123', encoding='utf-8'))
result = obj.hexdigest()
print(result)

# 防撞库操作
obj = hashlib.md5(bytes('qwertds', encoding='utf-8'))
obj.update(bytes('123', encoding='utf-8'))
result = obj.hexdigest()
print(result)
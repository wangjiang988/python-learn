#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
"""
验证码生成器,random随机生成数字
"""
import random

RANDOM_LIST = []  # 定义空列表,由于后续参数添加
for i in range(6):
    if i == 2:
        num = random.randrange(0, 10)
        RANDOM_LIST.append(str(num))
    else:
        temp = random.randrange(65, 91)
        ret = chr(temp)
        RANDOM_LIST.append(ret)

result = "".join(RANDOM_LIST)
print(result)


RANDOM_LIST = []  # 定义空列表,由于后续参数添加
for i in range(6):
    r = random.randrange(0, 5)
    # if i == r:
    if r == 2 or r == 4:
        num = random.randrange(0, 10)
        RANDOM_LIST.append(str(num))
    else:
        temp = random.randrange(65, 91)
        ret = chr(temp)
        RANDOM_LIST.append(ret)

result = "".join(RANDOM_LIST)
print(result)
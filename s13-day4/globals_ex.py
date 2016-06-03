#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

NAME = "Chen"


def show():
    a = 123
    print(locals())
    print(globals())

show()


# 获取字符串长度,在2中是以字节为统计,3中是以字符为统计
s = "中文"
print(len(s))

s = "中文"
b = bytes(s, encoding='utf-8')
print(len(b))

2.7 for "李杰"
3.5 for "李杰"
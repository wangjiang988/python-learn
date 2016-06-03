#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

r = divmod(97, 10)
print(r[0])
print(r[1])

n1, n2 = divmod(97, 10)

print(n1, n2)

# 判断对象是否是某个类的实例
s = [11, 22, 33]
r = isinstance(s, list)
print(r)


print(dir(list))
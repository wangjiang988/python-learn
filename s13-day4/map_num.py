#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

li = [11, 22, 33, 44, 55]


def f1(args):
    result = []
    for i in args:
        result.append(100 + i)
    return result

r = f1(li)
print(list(r))


# map 将函数返回值添加到结果中
li = [11, 22, 33, 44, 55]


def f2(a):
    return a + 100

result = map(f2, li)
print(list(result))

# lambda
li = [11, 22, 33, 44, 55]
result = map(lambda a: a + 100, li)
print(list(result))
#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 通过递归完成阶乘


def func(num):
    if num == 1:
        return 1
        # return True == return 1
    return num * func(num - 1)


x = func(7)
print(x)

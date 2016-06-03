#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 普通装饰器函数传递万能参数


def outer(func):
    def inner(*args, **kwargs):
        print("before")
        r = func(*args, **kwargs)
        print("after")
        return r
    return inner


@outer
def f1(args):
    print(args)
    return "砍你"

f1("fafafa")


@outer
def f2(args1, args2):
    print(args1, args2)
    print("F2")

f2(11, 22)
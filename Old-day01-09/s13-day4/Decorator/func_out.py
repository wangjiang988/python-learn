#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

"""
装饰器： @+函数名
功能：
1、自动执行outer函数并且将它下面的函数名f1当作参数传递
2、将outer函数的返回值，重新赋值给f1
"""


# 完整版装饰器
def outer(func):
    def inner():
        print("before")
        r = func()
        print("after")
        return r  # 一个函数遇到return之后,下面就不执行了.
    return inner


@outer
def f1():
    print("F1")
    return "砍你"

f1()


@outer
def f2():
    print("F2")


@outer
def f100():
    print("F100")
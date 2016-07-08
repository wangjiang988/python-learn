#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


# class Name:
#     country = "中国"
#
#     def __init__(self, name):
#         self.name = name
#
#     # 普通方法, 由对象去调用执行
#     def show(self):
#         print(self.name)
#
#     # 静态方法
#     @staticmethod
#     def f1(arg1, arg2):
#         # 静态方法, 由类调用执行
#         print(arg1, arg2)
#
#
# Name.f1(111, 222)  # 静态字段调用,通过类调用


class Name:
    country = "中国"

    def __init__(self, name):
        self.name = name

    # 普通方法, 由对象去调用执行
    def show(self):
        print(self.name)

    # 静态方法
    @staticmethod
    def f1(cla, arg1, arg2):
        # 静态方法, 由类调用执行(当方法内部不需要对象中封装的值时,可以将方法写成静态方法)
        print(arg1, arg2)

    @classmethod
    def f2(cls):  # class
        # cls  # 类名, () 创建对象
        print(cls)


# Name.f1(111, 222)  # 静态字段调用,通过类调用
Name.f1(Name, 1, 2)
Name.f2()
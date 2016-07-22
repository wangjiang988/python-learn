#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
# 面向对象关系,可以封装对象,对象嵌套对象


class c1:
    def __init__(self, name, obj):
        self.name = name
        self.obj = obj


class c2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)


c2_obj = c2("aa", 11)
c1_obj = c1("aaa", c2_obj)

print(c1_obj.obj.age)


class c1:
    def __init__(self, name, obj):
        self.name = name
        self.obj = obj


class c2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        return 123


class c3:
    def __init__(self, a1):
        self.money = 123
        self.aaa = a1


c2_obj = c2("aa", 11)
# c2_obj 是c2类型
# - name = 'aa'
# - age = 11
c1_obj = c1("aaa", c2_obj)
# c1_obj 是c2类型
# - name = 'aaa'
# - obj = c2_obj
c3_obj = c3(c1_obj)
# print(c3_obj.aaa, type(c3_obj.aaa))
# 使用c3_obj获取c3的name值
print(c3_obj.aaa.obj.age)
# 使用c3_obj执行show方法
s = c3_obj.aaa.obj.show()
print(s)

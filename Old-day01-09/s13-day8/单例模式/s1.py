#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
# goF设计模式

# 单例模式
# 用来创建单个实例, 通过classmethod构造单例模式


class Foo:

    instance = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_instance(cls):
        # cls 类名
        if cls.instance:
            return cls.instance
        else:
            obj = cls('alex')  # 值一般是固定的
            cls.instance = obj
            return obj

obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)


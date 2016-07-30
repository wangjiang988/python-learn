#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


class Foo:

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 垃圾回收方法, 析构方法
    def __del__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("call")

    def __str__(self):
        # return self.name
        return "%s - %d" % (self.name, self.age)

    def __getitem__(self, item):
        print(item.start)
        print(item.stop)
        print(item.step)
        print(type(item))
        return 123

    def __setitem__(self, key, value):
        print(type(key), type(value))
        return "setitem"

    def __delitem__(self, key):
        print(type(key))
        return "delitem"
"""
obj = Foo()
obj()  # 对象加(),执行call
Foo()()
"""

"""
obj1 = Foo('alex', 73)
obj2 = Foo('aric', 84)
print(obj1)
print(obj2)

ret = str(obj1)
print(ret)


# 获取对象中封装的数据
print(obj1.__dict__)
print(Foo.__dict__)
"""

obj = Foo('alex', 73)

# ret = obj['ad']
ret = obj[1:2:3]
print(ret)

# obj['k1'] = 111
obj[1:4] = [11, 22, 33, 44]
# print(obj['k1'])

# del obj['k1']
del obj[1::4]




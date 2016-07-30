#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
import commons

# 字符串反射

# import commons as obj
# obj.login()
#
# obj = __import__("commons")
# obj.login()



"""
python中的反射功能是由以下四个内置函数提供：hasattr、getattr、setattr、delattr，改四个函数分别用于对对象内部执行：检查是否含有某成员、获取成员、设置成员、删除成员。

class Foo(object):

    def __init__(self):
        self.name = 'chenliang'

    def func(self):
        return 'func'

obj = Foo()

# #### 检查是否含有成员 ####
hasattr(obj, 'name')
hasattr(obj, 'func')

# #### 获取成员 ####
getattr(obj, 'name')
getattr(obj, 'func')

# #### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)

# #### 删除成员 ####
delattr(obj, 'name')
delattr(obj, 'func')
http://www.cnblogs.com/wupeiqi/articles/5017742.html
"""


def run():
    inp = input("请输入你要访问的URL: ")
    # 反射: 利用字符串的形式去对象(默认--模块)中操作(寻找/检查/设置)成员
    # delattr()
    # setattr()
    if hasattr(commons, inp):  # 查看是否存在属性
        func = getattr(commons, inp)
        func()
    else:
        print(404)

if __name__ == '__main__':
    count = 0
    while count < 10:
        run()
        count += 1
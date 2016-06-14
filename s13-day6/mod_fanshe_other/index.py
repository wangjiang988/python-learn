#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
# import commons

# 模块反射

# import commons as obj
# obj.login()
#
# obj = __import__("commons")
# obj.login()


def run():
    inp = input("请输入你要访问的URL: ")
    # 反射: 利用字符串的形式去对象(默认--模块)中操作(寻找/检查/设置)成员
    # delattr()
    # setattr()
    m, f = inp.split('/')
    obj = __import__("lib." + m, fromlist=True)  # 导入路径
    if hasattr(obj, f):  # 查看是否存在属性
        func = getattr(obj, f)
        func()
    else:
        print(404)

if __name__ == '__main__':
    count = 0
    while count < 10:
        run()
        count += 1
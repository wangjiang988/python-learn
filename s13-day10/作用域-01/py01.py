#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 知识点一: Python中无块级作用域

if 1 == 1:
    name = 'day10'

print(name)

for i in range(10):
    num = i

print(num)

# 知识点二: Python中以函数为作用域


# def func():
#     string = 'day10'
#
# func()  # 不能执行
# print(string)  # 不能执行


# 知识点三: Python中存在作用域链条, 由内向外找, 直到找不到报错
name = 'alex'


def f1():
    print(name)


def f2():
    name = 'eirc'
    f1()


f2()

# Python的作用域在执行之前已经确定下来

name = 'alex'


def f1():
    print(name)


def f2():
    name = 'eirc'
    return f1


ret = f2()
ret()

# for 循环+if 判断
li1 = [x + 100 for x in range(10)]
li2 = [x + 100 for x in range(10) if x > 6]
print(li2)


# 面试题
li = [lambda: x for x in range(10)]
# li 为列表类型
# li 列表中的元素: [函数, 函数, 函数...]
# 函数在没有执行前, 内部代码不执行.
# ? li[], 函数
# ? 函数()
# 返回值是????
print(li[0]())

li = []

for i in range(10):
    def f1():
        return i

    li.append(f1)
# li 是列表, 内部元素是相同功能的函数
print(li[0]())
print(li[1]())


li = []

for i in range(10):
    def f1(x=i):  # 关键点在于执行还是没有执行
        return x

    li.append(f1)
# li 是列表, 内部元素是相同功能的函数
print(li[0]())
print(li[1]())


#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 函数返回True,将元素添加到结果中.获取列表中大于22的数


def f1(args):
    result = []

    for item in args:
        if item > 22:
            result.append(item)

    return result

li = [11, 22, 33, 44, 55]
ret = f1(li)
print(ret)


# 利用filter,filter内部,循环第二个参数
# tesult = []
# for item in 第二个参数:
#     r = 第一个参数(item)
#     if r:
#         result(item)
# return result
# 循环第二个参数,让每个循环元素执行函数,如果函数返回是True,表示元素合法,就将符合条件的元素扔到ret
def f2(a):
    if a > 22:
        return True

li = [11, 22, 33, 44, 55]

ret = filter(f2, li)
print(list(ret))

# 自动return
f1 = lambda a: a > 30
ret = f1(90)
print(ret)

# 通过lambda实现相同的功能
li = [11, 22, 33, 44, 55]
result = filter(lambda a: a > 33, li)
print(list(result))
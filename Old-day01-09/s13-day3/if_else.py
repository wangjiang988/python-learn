#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 三元运算(三目运算) if else的简写

if 1 == 1:
    name = 'admin'
else:
    name = 'SB'
print(name)

# 如果1==1成立,让if前面的值name=admin,
# 否则让if前面的变量name=SB
name = 'admin' if 1 == 1 else 'SB'
print(name)


# lambda的表达式
def f1(a1):
    return a1 + 100


ret1 = f1(10)
print(ret1)

f2 = lambda a1, a2: a1 + a2 + 100
ret2 = f2(10, 19)
print(ret2)

f3 = lambda a1, a2=9: a1 + a2 + 100
ret3 = f3(10)
print(ret3)

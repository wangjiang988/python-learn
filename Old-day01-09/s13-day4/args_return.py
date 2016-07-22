#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

li = [11, 22, 33, 44]


def f1(args):
    args.append(55)

# 函数默认值返回None,参数默认传递引用
# li = f1(li)
# print(li)  # 返回值为None


# f1(li)
# print(li)

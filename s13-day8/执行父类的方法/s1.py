#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


class C1:
    def f1(self):
        print("c1.f1")


class C2(C1):
    def f1(self):
        # 主动执行父类的f1方法
        super(C2, self).f1()
        print('c2.f1')

obj = C2()
obj.f1()

# 用途, 用于定制功能, 扩展功能
#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
# 特性, 单继承简单入门
# 所以，对于面向对象的继承来说，其实就是将多个类共有的方法提取到父类中，子类仅需继承父类而不必一一实现每个方法。


class F1:  # F1父类, 基类
    def show(self):
        print("show")

    def foo(self):
        print(self.name)


class F2(F1):  # F2子类, 派生类
    def __init__(self, name):
        self.name = name

    def bar(self):
        print("bar")

    def show(self):  # 同时执行show方法的适合, 子类优先级最高
        print("F2.show")


class F3(F2):
    pass


obj = F2('alex')
# obj.bar()
# obj.show()
obj.foo()

# 继承都是自身优先级高, 遇到self通常先找子类, 再找父类


class S1:
    def F1(self):
        self.F2()

    def F2(self):
        pass


class S2(S1):
    def F3(self):
        self.F1()

    def F2(self):
        pass


obj = S2()
obj.F3()


# 多继承
# Python的类如果存在共同父类继承, 默认执行到共同父类的上层之后, 就会转向另外调用的子类继续执行
class C_2:
    def f2(self):
        print("C-1")


class C_1(C_2):
    def f2(self):
        print("C-1")


class C0(C_2):
    def f2(self):
        print("C0")


class C1(C0):
    def f1(self):
        print("C1")

    # def f2(self):
    #     pass


class C2(C_1):
    def f2(self):
        print("C2")


class C3(C2, C1):  # 按照继承关系来, 左边继承的优先执行
    def f3(self):
        print("C3")

obj = C3()
obj.f2()
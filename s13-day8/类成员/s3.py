#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
# 属性, 伪造字段的关联方式
# 通过方法完成分页功能


class Pager:
    def __init__(self, all_count):
        self.all_count = all_count

    @property
    def all_pager(self):
        a1, a2 = divmod(self.all_count, 10)
        if a2 == 0:
            return a1
        else:
            return a1 + 1

    @all_pager.setter
    def all_pager(self, value):
        print(value)

    @all_pager.deleter
    def all_pager(self):
        print('del all_pager')

p = Pager(101)
# print(p.all_count)  # 字段
# p.all_count = 102
# result = p.all_pager() # 方法
# print(result)
# 其实就是加括号与不加括号的形式

# 字段获取
ret = p.all_pager  # 函数通过字段形式访问
print(ret)

# 字段设置, 属性具备字段设置
# 对于属性来说,想要被设置,需要定义
p.all_pager = 111

# 字段删除, 属性具备字段删除
del p.all_count

# 另外一种属性方式


class Pager:
    def __init__(self, all_count):
        self.all_count = all_count

    def f1(self):
        return 123

    def f2(self, value):
        print(value)

    def f3(self):
        pass

    foo = property(fget=f1, fset=f2, fdel=f3)

p = Pager(101)

# result = p.foo
# print(result)

p.foo = 'alex'
result = p.foo
print(result)
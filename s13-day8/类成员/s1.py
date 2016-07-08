#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 字段:


class Foo:
    # 字段 (静态字段)
    CC = 123

    def __init__(self):
        # 通称为字段(普通字段)
        self.name = 'alex'  # 保存在对象里

    def show(self):
        print(self.name)


# 写一个类, 每个省份创建一个对象

class Name:

    def __init__(self, name):
        self.name = name
        self.country = "中国"

obj1 = Name('河南')
obj2 = Name('河北')
obj3 = Name('山东')
obj4 = Name('黑龙江')

# 上面这种方式可以看出,每个对象中都会有一个中国, 这样的话会比较耗用内存资源


# 优化, 内存占用率就会较低
class Name:
    country = "中国"

    def __init__(self, name):
        self.name = name

# 一般情况下: 自己访问自己的字段
# 规则:
#   -- 普通的字段只能用对象访问
#   -- 静态字段只能用类访问(万不得已的时候可以是用对象访问)
obj1 = Name('河南')
print(obj1.name)  # 对象访问自己的字段
print(Name.country)  # 类访问自己的字段
print(obj1.country)  # 对象可以访问类里面的静态字段(不推荐)
obj2 = Name('河北')
obj3 = Name('山东')
obj4 = Name('黑龙江')

# 经过优化后, 我们让所有的对象都去class里面调用静态字段, 这样在内存中就不会重复写入
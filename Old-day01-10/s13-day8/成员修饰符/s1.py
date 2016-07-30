#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 成员修饰符
# 字段

# 公共的
# 类的外部进行调用
class Foo:
    def __init__(self, name):
        self.name = name

obj = Foo('alex')
print(obj.name)

# 类的内部进行调用
class Foo:
    def __init__(self, name):
        self.name = name

    def f1(self):
        print(self.name)

obj = Foo('alex')
obj.f1()



# 私有的普通字段
class Foo:
    def __init__(self, name):
        self.__name = name

    def f1(self):
        print(self.__name)

obj = Foo('alex')
# print(obj.__name)  # 外部不能访问

obj.f1()  # 内部方法调用成功

# 私有普通字段继承
class Foo:
    def __init__(self, name):
        self.__name = name

    def f1(self):
        print(self.__name)


class Bar(Foo):
    def f2(self):
        print(self.__name)

obj = Bar('alex')
obj.f2()  # 私有的只有自己本身能访问自己,继承也不行
obj.f1()  # 自己是可以的


# 私有的静态字段
class Foo:
    __cc = "123"

    def __init__(self, name):
        self.__name = name

    def f1(self):
        print(self.__name)

    @staticmethod
    def f3():
        print(Foo.__cc)

print(Foo.__cc)  # 不能访问
obj = Foo('dddd')
obj.f3()  # f3可以访问

Foo.f3()  # 加@staticmethod可以访问


#
class Name:
    __country = "中国"

    def __init__(self, name):
        self.__name = name

    # 普通方法, 由对象去调用执行
    def show(self):
        print(self.__name)

    def f1(self):
        print(self.__name)


obj = Name('alex')
print(obj._Name__name)  # 不到万不得已不要在外部强制访问私有成员


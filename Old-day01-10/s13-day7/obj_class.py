#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


class SQLHelper:
    def __init__(self, host, username, password):
        # print("自动执行init方法")
        self.hhost = host
        self.uname = username
        self.passwd = password

    def fetch(self, sql):
        print(sql)

    def create(self, sql):
        pass

    def remove(self, sql):
        pass

    def modify(self, sql):
        pass


obj1 = SQLHelper('s1.salt.com', 'chenliang', '123456')
obj2 = SQLHelper('s2.salt.com', 'shenlong', '654321')
obj1.fetch("select * from A")
obj2.fetch("select * from B")

# 练习  类里面不分顺序执行

"""
练习一：在终端输出如下信息

小明，10岁，男，上山去砍柴
小明，10岁，男，开车去东北
小明，10岁，男，最爱大保健
老李，90岁，男，上山去砍柴
老李，90岁，男，开车去东北
老李，90岁，男，最爱大保健
老张...
"""


# 面向过程
def kanchai(name, age, gender):
    print("%s,%s岁,%s,上山去砍柴" % (name, age, gender))


def qudongbei(name, age, gender):
    print("%s,%s岁,%s,开车去东北" % (name, age, gender))


def dabaojian(name, age, gender):
    print("%s,%s岁,%s,最爱大保健" % (name, age, gender))


kanchai('小明', 10, '男')
qudongbei('小明', 10, '男')
dabaojian('小明', 10, '男')

kanchai('老李', 90, '男')
qudongbei('老李', 90, '男')
dabaojian('老李', 90, '男')


# 面向对象
class Foo:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def kanchai(self):
        print("%s,%s岁,%s,上山去砍柴" % (self.name, self.age, self.gender))

    def qudongbei(self):
        print("%s,%s岁,%s,开车去东北" % (self.name, self.age, self.gender))

    def dabaojian(self):
        print("%s,%s岁,%s,最爱大保健" % (self.name, self.age, self.gender))


xiaoming = Foo('小明', 10, '男')
xiaoming.kanchai()
xiaoming.qudongbei()
xiaoming.dabaojian()

laoli = Foo('老李', 90, '男')
laoli.kanchai()
laoli.qudongbei()
laoli.dabaojian()

# 练习二: 游戏人生程序
"""
1、创建三个游戏人物，分别是：

苍井井，女，18，初始战斗力1000
东尼木木，男，20，初始战斗力1800
波多多，女，19，初始战斗力2500
2、游戏场景，分别：

草丛战斗，消耗200战斗力
自我修炼，增长100战斗力
多人游戏，消耗500战斗力
"""


# #####################  定义实现功能的类  #####################

class Person:
    def __init__(self, na, gen, age, fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight = fig

    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""

        self.fight -= 200

    def practice(self):
        """注释：自我修炼，增长100战斗力"""

        self.fight += 200

    def incest(self):
        """注释：多人游戏，消耗500战斗力"""

        self.fight -= 500

    def detail(self):
        """注释：当前对象的详细情况"""

        temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s" % (self.name, self.gender, self.age, self.fight)
        print(temp)


# #####################  开始游戏  #####################

cang = Person('苍井井', '女', 18, 1000)  # 创建苍井井角色
dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
bo = Person('波多多', '女', 19, 2500)  # 创建波多多角色

cang.incest()  # 苍井空参加一次多人游戏
dong.practice()  # 东尼木木自我修炼了一次
bo.grassland()  # 波多多参加一次草丛战斗

# 输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()

cang.incest()  # 苍井空又参加一次多人游戏
dong.incest()  # 东尼木木也参加了一个多人游戏
bo.practice()  # 波多多自我修炼了一次

# 输出当前所有人的详细情况
cang.detail()
dong.detail()
bo.detail()

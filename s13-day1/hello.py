#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

"""
print("hello world")

name = "Chen Liang"
age = 26

print(name, age)
"""

"""
name = "Chen Lang"
age = 21
province = "Si Chuan"
company = "HaiZhi"
GfAge = 24
daughter_age = 1
_name = "Fname"
"""

# Py开发规范:

# 每一行不超过80个字符
# 注释#号, ```, """号

# Case1: 读取用户信息
# Py2.7需要用raw_input
# Py3用input
# 浮点表示: %f
# 字符串表示: %s
# 数字表示: %d

# 数字赋值需用int将字符串转换为数字

name = input("请输入您的姓名: ")
age = int(input("请输入您的年龄: "))
job = input("请输入你的职位: ")

"""
print("Name is: ", name)
print("Age is:", age)
print("Job is: ", job)
"""

msg = """
用户%s输入的信息如下 :
---------------------
姓名: %s
年龄: %d
职位: %s
---------END---------
""" % (name, name, age, job)

print(msg)


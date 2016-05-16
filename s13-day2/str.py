#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

#  字符串格式化,规范输入
username = input("Username: ")
if username.strip() == 'alex':
    print("Welcome %s") % username

#  --->通过,号组成一个列表
names = "alex,jack,rain"
name2 = names.split(",")
print(name2)

#  --->按照|来进行合并
print( "|".join(name2))

name = "Alex Li"
print('' in name) # 判断字符串中是否有空格

name = "alex li"
print(name.capitalize()) # 首字母大写

# name.format()  # 字符串格式化

msg = "Hello, {name}, it's been a long {age} since last time sopke..."
msg2 = msg.format(name='Linux', age=333)
print(msg2)

msg2 = "hebe{0}, helm{1}"
print(msg2.format('alex', 33))

print(name[2:4])

name = "Chen Liane"
print(name.center(40, "-"))

print(name.find('l')) # 查找字符串索引,不存在则返回-1

#  --->数字,字母判断
age = input("Your Age: ")
if age.isdigit():
    age = int(age)
    print(age)
else:
    print("Invalid data type")

name = 'alex!sf'
print(name.isalnum())  # 不能包含特殊字符

print(name.endswith('df'))  # 以...结尾

print(name.startswith('dfsd'))  # 以...开始

print(name.upper().lower())  # 大小写转换
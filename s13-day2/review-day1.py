#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-

# H&M & UNIQLO
# 香水：名创优品

# 变量使用

# raw_input 2.7
# input 

import getpass

# user = 'admin'
# passwd = 'alex123'

# 变量新方法定义：
user, passwd = 'admin', 'alex123'

username = input("username: ")  # 3.0
password = getpass.getpass("passwd: ")  # 3.0

if username == user and password == passwd:
    print("welcome !")
else:
    print("wrong username and password!")

# 多重if判断
real_age = 25
guess_age = int(input("age: "))

for x in range(10):
    if x >= 3:
        break
    if guess_age > real_age:
        print("smaller")
    elif guess_age < real_age:
        print("bigger")
    else:
        print("got it")
        break

# 信息调用
name = input("username: ")
age = int(input("age: "))
job = input("job: ")

msg = """
Information of below person: 
NAME: %s
AGE: %d
JOB: %s
""" % (name, age, job)

# 变量
name = 'admin'

# 常量(命名规则，全部为大写)
MYSQL_CONNECTION = 20

# import 模块名，标准库可以直接导入，第三方库需下载安装
# pip 安装各种python模块的命令
# sudo pip install pandas # 安装pandas模块

import os

os.system(df)
os.popen("ifconfig").read()

import sys

sys.path
# 全局模块存放目录site-packages,dist-packages

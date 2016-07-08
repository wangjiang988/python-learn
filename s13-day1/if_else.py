#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 多重if判断
# import getpass
"""
user = 'admin'
passwd = 'alex3714'

username = input("Please Input Username: ")
password = input("Please Input Password: ")
# password = getpass.getpass("Please Input Password: ")

if user == username:
    print("username is correct...")
    if passwd == password:
        print("welcome login...")
    else:
        print("password is invalid...")
else:
    print("username is invalid...")

"""

# 优化代码,减少多重判断

user = 'admin'
passwd = 'alex3714'

username = input("Please Input Username: ")
password = input("Please Input Password: ")
# password = getpass.getpass("Please Input Password: ")

if user == username and passwd == password:
    print("Welcome login...")
else:
    print("Invalid username or password...")
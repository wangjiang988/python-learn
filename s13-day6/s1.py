#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
"""
我是注释
"""
import s2
import os
import sys

# print(vars(s2))

# 模块中的特殊变量
print(__doc__)  # 获取注释

print(__cached__)  # 自解码存放位置pycache

print(__file__)  # 获取当前py文件所在路径, 取决于当前执行文件所在位置

print(os.path.abspath(__file__))  # 获取绝对路径
print(os.path.dirname(os.path.abspath(__file__)))  # 获取目录的上一级目录

ret = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(ret)  # 添加代码的路径到path

sys.path.append(ret)

print(__package__)  # 获取模块所在的目录

# 一般在主文件中调用
print(__name__)  # 只有执行当前文件时候,当前文件的特殊变量__name__==__main__否则不等于__main__
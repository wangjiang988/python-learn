#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

"""
写一个列表,找出有多少个9,把它改成9999,同时找出所有的34,把它删掉
"""

name = [9, 2, 3, 4, 5, 3, 2, 1, 2, 34, 3, 9, 1, 9, 34, 9, 34, 21, 43, 34, 9]
for i in range(name.count(9)):
    ele_index = name.index(9)
    name[ele_index] = 9999
print(name)

for i in range(name.count(34)):
    ele_index = name.index(34)
    name.pop(ele_index)
print(name)

# Update
name = [9, 2, 3, 4, 5, 3, 2, 1, 2, 34, 3, 9, 1, 9, 34, 9, 34, 21, 43, 34, 34, 34, 9]
index = 0
for i in range(name.count(9)):
    ele_index = name.index(9, index)
    name[ele_index] = 9999
    index = ele_index
print(name)

index = 0
for i in range(name.count(34)):
    ele_index = name.index(34, index)
    name.pop(ele_index)
    index = ele_index
print(name)
#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

"""
写一个列表,列表里面包含本组所有成员名字, 往中间位置插入两个邻组成员名字, \
取出第3-8的人的名称列表, 删除第7个人, 把刚才加入的那2个邻组的人一次性删除,
把组长的名字加上组长备注, 要求隔一个人打印一个人
"""

name = ["ChenLiang", "WuYanlong", "DuanGuanyang", "LiuKai", "ZhangXunan", "LuShuai", "JiXiang", "LiXuewen"]
print(name.insert(4,"HanDongxu"))
name.insert(4,"HuangXu")
name2 = name[3:8]
print(name2)

name.remove(name[7])
print(name)

print(name[5:7])
del_name = name[5:7]
for i in del_name:
    name.remove(i)
print(name)

# del可以删除变量,列表 del name
index_num = name.index("DuanGuanyang")
del name[index_num:index_num+2]
print(name)

name_index = name.index("WuYanlong")
name = name[name_index] + "(组长)"
print(name)


# 步长取值
name[::2]

init = 0
for i in name:
    name[init]
    init += 2
    continue


name.pop()

import copy
name = copy.deepcopy()
#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import configparser

config = configparser.ConfigParser()
config.read("config.conf", encoding='utf-8')


# #########Read#########
secs = config.sections()
# 返回所有section
print("config's sections: ", secs)

# 获取单个section的option
options = config.options('global')
print("global's option: ", options)

# 获取所有section的option
for option in secs:
    options = config.options(option)
    print("%s option: %s" % (option, options))

# 获取单个section的所有item
item_list = config.items('database')
print("database的item为: %s" % item_list)

# 获取单个section的value
val = config.get('mongo', 'host')
print("mongo的host值为: %s" % val)

val = config.getint('redis', 'port')
print("redis的port值为: %s" % val)

# ######### Update,Write #########
sec = config.remove_section("redis")
print(sec)
config.write(open("config.conf", "w"))

# 查看配置文件中是否有test的section,没有则添加
sec1 = config.has_section('test')
print(sec1)
sec2 = config.add_section('test')
print(sec2)

# 将内存中的更新写入文件
config.write(open("config.conf", "w"))

# 将redis对应的port值改为6666
config.set("mongo", "port", "6666")
config.write(open("config.conf", "w"))

# 移除databse对用的charset选项,并保存文件
config.remove_option("database", "charset")
config.write(open("config.conf", "w"))
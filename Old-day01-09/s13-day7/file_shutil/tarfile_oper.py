#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import tarfile

# 压缩
tar = tarfile.open("your.tar", "w")
tar.add("test1.xml", arcname='tar01.log')
tar.add("test2.xml", arcname="tar02.log")
tar.close()


# 解压
tar = tarfile.open("your.tar", "r")
# tar.extractall()  # 解压所有文件
# tar.extract()  # 解压单个文件

for item in tar.getmembers():  # 获取压缩包文件内容
    # print(item, type(item))
    print("\033[34;1m当前tar文件中有如下内容: %s \033[0m" % item)

input_file = input("\033[32;1m请输入你要解压的文件: \033[0m")

obj = tar.getmember(input_file)
# print(obj, type(obj))
tar.extract(obj)
tar.close()
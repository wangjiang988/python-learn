#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 高级的文件,文件夹,压缩包处理模块

import zipfile

# 压缩文件
z = zipfile.ZipFile("ceshi.zip", "w")  # a 追加文件
z.write("test1.xml")
z.write("test2.xml")
z.close()

# 解压文件
z = zipfile.ZipFile("ceshi.zip", "r")
# z.extractall()  # 解压所有文件
# z.extract()  # 解压单个文件
for item in z.namelist():  # 查看压缩文件包含的内容
    print("\033[34;1m当前压缩包有如下文件: %s\033[0m" % item)

input_file = input("\033[32;1m请输入你要解压的文件: \033[0m")

z.extract(input_file)
z.close()

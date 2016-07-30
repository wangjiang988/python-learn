#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
# http://www.cnblogs.com/wupeiqi/articles/5501365.html

from xml.etree import ElementTree as ET


# ############ 解析方式一 ############
"""
# 打开文件，读取XML内容
str_xml = open('tree.xml', 'r').read()

# 将字符串解析成xml特殊对象，root代指xml文件的根节点
root = ET.XML(str_xml)
"""
# ############ 解析方式二 ############

# 直接解析xml文件
tree = ET.parse("tree.xml")

# 获取xml文件的根节点
root = tree.getroot()

# 顶层标签
# print(root.tag)  # 获取节点名
# print(root.attrib)  # 获取属性

# 遍历XML文档的所有内容
# 遍历XML文档的第二层
for child in root:
    # 第二层节点的标签名称和标签属性
    print(child.tag, child.attrib)
    # 遍历XML文档的第三层
    for i in child:
        # 第二层节点的标签名称和内容
        print(i.tag, i.text)


# 遍历XML中指定的节点
# 遍历XML中左右的year节点
for node in root.iter("year"):
    # 节点的标签名称和内容
    print(node.tag, node.text)



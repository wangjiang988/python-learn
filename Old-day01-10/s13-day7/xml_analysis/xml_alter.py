#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
from xml.etree import ElementTree as ET

# 修改节点中内容
# 由于修改的节点时，均是在内存中进行，其不会影响文件中的内容。所以，如果想要修改，则需要重新将内存中的内容写到文件。
# 解析字符串方式,修改,保存


def str_parser():
    # ######### 解析方式一 #########

    # 打开文件,读取XML内容
    string_xml = open("tree.xml", "r").read()

    # 将字符串解析成xml特殊对象,root代指xml文件的根节点
    root = ET.XML(string_xml)

    # ######### 操作 #########

    # 顶层标签打印
    print(root.tag)

    # 循环所有的year节点
    for node in root.iter('year'):
        # 将year节点中的内容自增一
        new_year = int(node.text) + 1
        node.text = str(new_year)

        # 设置属性
        node.set('name', 'alex')
        node.set('age', '18')
        # 删除属性
        del node.attrib['name']

    # ############ 保存文件 ############
    tree = ET.ElementTree(root)
    tree.write("new_str.xml", encoding='utf-8')


def file_parser():
    # 解析文件方式,修改,保存
    # ############ 解析方式二 ############

    # 直接解析xml文件
    tree = ET.parse("tree.xml")

    # 获取xml文件的根节点
    root = tree.getroot()

    # ############ 操作 ############

    # 顶层标签
    print(root.tag)

    # 循环所有的year节点
    for node in root.iter('year'):
        # 将year节点中的内容自增一
        new_year = int(node.text) + 1
        node.text = str(new_year)

        # 设置属性
        node.set('name', 'alex')
        node.set('age', '18')
        # 删除属性
        del node.attrib['name']

    # ############ 保存文件 ############
    tree.write("new_file.xml", encoding='utf-8')


str_parser()
file_parser()
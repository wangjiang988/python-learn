#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

from xml.etree import ElementTree as ET


# 删除节点

def del_str():
    # ############ 解析字符串方式打开 ############

    # 打开文件，读取XML内容
    str_xml = open('tree.xml', 'r').read()

    # 将字符串解析成xml特殊对象，root代指xml文件的根节点
    root = ET.XML(str_xml)

    # ############ 操作 ############

    # 顶层标签
    print(root.tag)

    # 遍历data下的所有country节点
    for country in root.findall('country'):
        # 获取每一个country节点下rank节点的内容
        rank = int(country.find('rank').text)

        if rank > 50:
            # 删除指定country节点
            root.remove(country)

    # ############ 保存文件 ############
    tree = ET.ElementTree(root)
    tree.write("new_str.xml", encoding='utf-8')


def del_file():
    # ############ 解析文件方式 ############

    # 直接解析xml文件
    tree = ET.parse("tree.xml")

    # 获取xml文件的根节点
    root = tree.getroot()

    # ############ 操作 ############

    # 顶层标签
    print(root.tag)

    # 遍历data下的所有country节点
    for country in root.findall('country'):
        # 获取每一个country节点下rank节点的内容
        rank = int(country.find('rank').text)

        if rank > 50:
            # 删除指定country节点
            root.remove(country)

    # ############ 保存文件 ############
    tree.write("new_file.xml", encoding='utf-8')


del_str()
del_file()

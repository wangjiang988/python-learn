#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# http://www.cnblogs.com/wupeiqi/articles/5501365.html

from xml.etree import ElementTree as ET


def create_xml_one():
    # 创建根节点
    root = ET.Element("famliy")

    # 创建节点大儿子
    son1 = ET.Element('son', {'name': '儿1'})
    # 创建小儿子
    son2 = ET.Element('son', {"name": '儿2'})

    # 在大儿子中创建两个孙子
    grandson1 = ET.Element('grandson', {'name': '儿11'})
    grandson2 = ET.Element('grandson', {'name': '儿12'})
    son1.append(grandson1)
    son1.append(grandson2)

    # 把儿子添加到根节点中
    root.append(son1)
    root.append(son1)

    tree = ET.ElementTree(root)
    tree.write('oooo.xml', encoding='utf-8', short_empty_elements=False)


def create_xml_two():
    # 创建根节点
    root = ET.Element("famliy")

    # 创建大儿子
    # son1 = ET.Element('son', {'name': '儿1'})
    son1 = root.makeelement('son', {'name': '儿1'})
    # 创建小儿子
    # son2 = ET.Element('son', {"name": '儿2'})
    son2 = root.makeelement('son', {"name": '儿2'})

    # 在大儿子中创建两个孙子
    # grandson1 = ET.Element('grandson', {'name': '儿11'})
    grandson1 = son1.makeelement('grandson', {'name': '儿11'})
    # grandson2 = ET.Element('grandson', {'name': '儿12'})
    grandson2 = son1.makeelement('grandson', {'name': '儿12'})

    son1.append(grandson1)
    son1.append(grandson2)

    # 把儿子添加到根节点中
    root.append(son1)
    root.append(son1)

    tree = ET.ElementTree(root)
    tree.write('oooo.xml', encoding='utf-8', short_empty_elements=False)


def create_xml_three():
    # 创建根节点
    root = ET.Element("famliy")

    # 创建节点大儿子
    son1 = ET.SubElement(root, "son", attrib={'name': '儿1'})
    # 创建小儿子
    son2 = ET.SubElement(root, "son", attrib={"name": "儿2"})

    # 在大儿子中创建一个孙子
    grandson1 = ET.SubElement(son1, "age", attrib={'name': '儿11'})
    grandson1.text = '孙子'

    et = ET.ElementTree(root)  # 生成文档对象 注释信息
    et.write("test.xml", encoding="utf-8", xml_declaration=True, short_empty_elements=False)


# 由于原生保存的XML时默认无缩进，如果想要设置缩进的话， 需要修改保存方式：

def suojin_xml():
    from xml.etree import ElementTree as ET
    from xml.dom import minidom

    def prettify(elem):
        """将节点转换成字符串，并添加缩进。
        """
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="\t")

    # 创建根节点
    root = ET.Element("famliy")

    # 创建大儿子
    # son1 = ET.Element('son', {'name': '儿1'})
    son1 = root.makeelement('son', {'name': '儿1'})
    # 创建小儿子
    # son2 = ET.Element('son', {"name": '儿2'})
    son2 = root.makeelement('son', {"name": '儿2'})

    # 在大儿子中创建两个孙子
    # grandson1 = ET.Element('grandson', {'name': '儿11'})
    grandson1 = son1.makeelement('grandson', {'name': '儿11'})
    # grandson2 = ET.Element('grandson', {'name': '儿12'})
    grandson2 = son1.makeelement('grandson', {'name': '儿12'})

    son1.append(grandson1)
    son1.append(grandson2)

    # 把儿子添加到根节点中
    root.append(son1)
    root.append(son1)

    raw_str = prettify(root)

    f = open("xxxoo.xml", 'w', encoding='utf-8')
    f.write(raw_str)
    f.close()

create_xml_one()
create_xml_two()
create_xml_three()
suojin_xml()
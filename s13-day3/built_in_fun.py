#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# abs 绝对值

n = abs(-1)
print(n)

# bool 为false的值
print(bool(None))
print(bool(0))
print(bool())
print(bool([]))
print(bool({}))
print(bool(()))

# all 所有值为真才为真
n = all([1, 2, 3, 4, 5])
print(n)

# any 任意一个为真才为真
n = any([1, 2, [], None])
print(n)

# ascii() 自动执行对象的__repr__方法
# class Foo:
#     def __repr__(self):
#         return "111"
#
#
# n = ascii(Foo())
# print(n)

# Decorator  # 10进制转换为2进制
# oct  # 10进制转换为8进行制
# hex  # 10进制转换为16进制
print("\033[31;1m10进制转换为2进制:\033[0m ", bin(5))
print("\033[31;1m10进制转换为8进行制:\033[0m ", oct(5))
print("\033[31;1m10进制转换为16进制:\033[0m ", hex(5))

# utf-8 一个汉字: 三个字节
# gbk 一个汉字: 两个字节
# bytes  # 想将字符串转换为字节类型,需要用bytes(转换的字符串, 按照什么编码)
s = "陈亮"  # 一个字节8位,一个汉字三个字节
#
n = bytes(s, encoding='utf-8')
print("\033[31;1mUTF-8转换字节为:\033[0m %s" % n)

n = bytes(s, encoding='gbk')
print("\033[31;1mGBK转换字节为:\033[0m %s" % n)

# bytearray()  # 创建字节数组

# 字节转化为字符串
new_str = str(bytes(s, encoding='utf-8'), encoding='utf-8')
print("\033[31;1m字节转化为字符串:\033[0m %s" % new_str)

# 文件操作
# 打开文件
# f = open("db", "r")  # 只读
# f = open("db", "w")  # 只写,会将文件先清空
# f = open("db", "x")  # 如果文件存在就报错,否则,创建并写内容
# f = open("db", "a")  # 追加内容.seek 标志位偏移
with open("db", "r", encoding='utf-8') as f:
    read_f = f.read()
    print("读取UTF-8编码的内容: ", read_f)

# f = open("db", "rb") # 告诉python直接使用二进制处理
with open("db", "rb") as f:
    read_f = f.read()
    print("读取二进制: ", read_f, type(read_f))

with open("db", "ab") as f:
    write_f = f.write(bytes("陈亮", encoding='utf-8'))
    print("写入二进制: ", write_f, type(write_f))

# f = open("db", "r+")  # 可读可写  **用的最多的**
# f = open("db", "w+")  # 可读可写
# f = open("db", "x+")  # 可读可写
# f = open("db", "a+")  # 可读可写
# 默认情况下,文件是有指针,当完全遍历一遍文件之后,指针的位置在文件末尾
# 如果打开模式无b,则read,按照字符读取
with open("db", "r+", encoding="utf-8") as f:
    data = f.read()
    print(data)
    # tell当前指针所在的位置(字节)
    print(f.tell())  # 获取当前指针的位置
    # 调整当前指针的位置(字节)
    f.seek(f.tell())  # 主动把指针调整到某个位置,永远以字节的方式去找位置
    # 当前指针位置开始向后覆盖
    f.write("777")
# 操作文件
# f.read()  # 通过源码查看文件
# 无参数,读取全部,有参数,b,按照字节,无b按照字符
# tell()  # 获取当前指针位置(字节)
# seek()  # 指针跳到指定位置(字节)
# write() # 写数据,b,字节,无b,字符
# fileno() # 文件描述符
# flush() # 强刷内容到硬盘
# readable() # 是否可读
# seekable() # 是否可以移动指针
# readline # 仅读取一行,
# writeable() # 是否可写
# truncate() # 截断,通过seek指针位置来清空
# for 循环文件对象 # 常用操作,文件读行
with open("db", "r") as f:
    for line in f:
        print(line)

# 关闭文件
# f.close()
# with open("db", "a") as f:
#    pass

# 通过with可以同时操作多个文件
with open("db1", "r", encoding='utf-8') as f1, open("db2", "w", encoding='utf-8') as f2:
    times = 0
    for line in f1:
        times += 1
        if times <= 10:
            f2.write(line)
        else:
            break

# 把一个文件的前10行,写到另外一个文件的后10行

# 修改alex到eric
with open("db1", "r", encoding='utf-8') as f1, open("db2", "w", encoding='utf-8') as f2:
    for line in f1:
        new_str = line.replace("admin", "st")
        f2.write(new_str)

with open("db1", "r", encoding='utf-8') as f1, open("db2", "w", encoding='utf-8') as f2:
    for line in f1:
        new_str = line.replace("admin", "st")
        f2.write(new_str)
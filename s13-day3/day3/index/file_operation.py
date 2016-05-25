#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import os
import json

"""
把文件按从上到下的顺序分为上部分,要处理部分,下部分;
step1: 上部分从haproxy.cfg文件写入-->new_haproxy.cfg
step2: 遇到要处理部分则写入-->get_list
step3: 下部分从haproxy.cfg文件写入-->new_haproxy.cfg
step4:  get_list入-->new_haproxy.cfg
"""


def get(backend):  # 定义get函数，并同时传入我们指定backend参数，此参数代表backend名
    flag = False  # 定义flag为False，目的是为了后面是否取可用的backend
    get_list = []  # 定义空列表，目的是为了后面将取出的backend信息存储在此列表里面
    with open('haproxy.cfg') as obj:  # 打开配置文件
        for line in obj:  # 一行行读取
            if line.strip() == "backend %s" % (backend):  # line.stri()去掉空格和换行符
                flag = True  # 读到要取的记录flage改为True
                continue  # 结束本次循环,下面代码不执行,开始new_的循环
            if flag and line.strip().startswith('backend'):  # 如果已经取到记录,则又读到backend开头的数据则不取
                flag = False
            if flag and line.strip():  # 判断flag为True,且不是空行(布尔值非空是True)
                get_list.append(line.strip())  # 把数据加入列表

    return get_list  # 返回值


def add(dict_info):  # 定义add函数，同时传入参数dict_info,字典参数里面包含要传入的server信息
    backend_title = dict_info.get("backend")  # 插入的backend的名称(变量初始化)
    context_title = "backend %s" % (backend_title)  # 插入backend整个字段(变量初始化)
    record_title = dict_info["record"]  # 要插入的记录(变量初始化)
    context_record = "server %s %s weight %s maxconn %s" % (
        record_title["server"], record_title["server"], record_title["weight"], record_title["maxconn"])
    get_list = get(backend_title)  # 把读取的记录放入列表(变量初始化)

    if get_list:  # 判断列表是否为空
        flag = False  # 标志位
        flag_write = False  # 标志位
        with open('haproxy.cfg', 'r') as read_obj, open('new_haproxy.cfg', 'w') as write_obj:
            for line in read_obj:
                if line.strip() == context_title:
                    write_obj.write("\n" + line)
                    flag = True
                    continue
                if flag and line.startswith('backend'):  # flag为True,如果在读到backend信息,则不处理
                    flag = False
                if flag:
                    for new_line in get_list:
                        if not flag_write:
                            temp = "%s%s" % (" " * 8, new_line)  # 把列表的记录赋值给temp
                            write_obj.write(temp)
                            flag_write = True
                else:
                    write_obj.write(line)

    else:  # 如果get_list为空
        with open('haproxy.cfg') as read_obj, open('new_haproxy.cfg', 'w') as write_obj:
            for line in read_obj:
                write_obj.write(line)
            write_obj.write("\n" + context_title + "\n")
            temp = " " * 8 + context_record + "\n"
            write_obj.write(temp)

    os.rename('haproxy.cfg', 'haproxy.cfg.bak')  # 将原文件配置文件改名备用文件为配置文件b
    os.rename('new_haproxy.cfg', 'haproxy.cfg')  # 将new_配置文件改名为配置文件


def delete(dict_info):  # 删除函数

    del_backend = dict_info["backend"]
    del_record = dict_info["record"]

    context_title = "backend %s" % (del_backend)
    context_record = "server %s %s weight %s maxconn %s" % (
        del_record["server"], del_record["server"], del_record["weight"], del_record["maxconn"])

    get_list = get(del_backend)

    if not get_list:
        return

    else:

        if context_record not in get_list:
            print("your server message is not exists")
            return

        else:
            get_list.remove(context_record)

        with open('haproxy.cfg', 'r') as read_obj, open('new_haproxy.cfg', 'w') as write_obj:
            flag = False
            flag_write = False
            for line in read_obj:
                if line.strip() == context_title:
                    write_obj.write(line)
                    flag = True
                    continue
                if flag and line.startswith('backend'):
                    flag = False
                if flag:
                    if not flag_write:
                        print(get_list)
                        for new_line in get_list:
                            temp = "%s%s\n" % (" " * 8, new_line)
                            write_obj.write(temp)
                        flag_write = True
                else:
                    write_obj.write(line)

    os.rename('haproxy.cfg', 'haproxy.cfg')
    os.rename('new_haproxy.cfg', 'haproxy.cfg')


s = '{"backend":"ttt.oldboy.org","record":{"server":"100.1.7.9","weight":"20","maxconn":"3000"}}'  # 要添加的记录信息

if __name__ == "__main__":  # 主函数,入口

    print(u"1.获取记录\n2.添加记录\n3.删除记录\n")  # 获取用户的操作选择
    select_num = input("请输入需要进行的操作编号:")

    if select_num == "1":  # 根据用户的选择，进行调用函数
        backend = input("请输入backend信息:")
        get_list = get(backend)
        for i in get_list:
            print("配置信息:%s" % i)
    else:
        print("请按以下格式输入:")
        print('{"backend":"ttt.oldboy.org","record":{"server":"100.1.7.9","weight":"20","maxconn":"3000"}}')
        data_str = input("请输入信息>>>")
        data_dict = json.loads(data_str)
        if select_num == "2":
            add(data_dict)
        elif select_num == "3":
            delete(data_dict)
        else:
            print("输入有误!!!!!")

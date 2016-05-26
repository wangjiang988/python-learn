#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import os
import json


def get(backend):
    """
    : 定义get函数，并同时传入我们指定backend参数，此参数代表backend名
    : 定义Flag为False，用于判断后面是否取可用的backend
    : 定义空列表，目的是为了后面将取出的backend信息存储在此列表里面
    : 打开配置文件
    : 读行
    : line.stri()去掉空格和换行符
    : 读到要取的记录Flag改为True
    : 结束本次循环,下面代码不执行,开始new的循环
    : 如果已经取到记录,则又读到backend开头的数据则不取
    : 判断flag为True,且不是空行(布尔值非空是True)
    : 把数据加入列表
    :return: 获取get_list值
    """
    flag = False
    get_list = []
    with open("haproxy.cfg", "r", encoding="utf-8") as obj:
        for line in obj:
            if line.strip() == "backend %s" % (backend):
                flag = True
                continue
            if flag and line.strip().startswith('backend'):
                flag = False
            if flag and line.strip():
                get_list.append(line.strip())
    return get_list


def add(dict_info):
    """
    : 获取backend的名称(变量初始化)
    : 获取backend整个字段(变量初始化)
    : 获取要插入的记录(变量初始化)
    : 只读打开主配置文件,同时以写的方式打开新添加文件
    : 循环读取配置文件同时往新文件里面写,line与backend信息相等,就写入value信息
    : 否则直接往文件末尾增加
    :return:
    """
    backend_name = dict_info.get("backend")
    title_name = "backend %s" % (backend_name)
    record_context = dict_info["record"]
    context_info = "server %s %s weight %s maxconn %s" % (
        record_context["server"], record_context["server"], record_context["weight"], record_context["maxconn"])
    flag = False
    temp = "%s%s\n" % (" " * 8, context_info)  # 把列表的记录赋值给temp,同时按照格式添加记录预留8个空格
    with open("haproxy.cfg", "r", encoding="utf-8") as obj_read, open("new_haproxy.cfg", "w", encoding='utf-8') as obj_write:
        for line in obj_read:
            obj_write.write(line)
            if flag is not True and line.strip() == title_name:
                obj_write.write(temp)
                flag = True

        if flag is not True:
            obj_write.write("\n" + title_name)
            obj_write.write("\n" + temp)

    os.rename('haproxy.cfg', 'haproxy.cfg.backup')  # 将haproxy.cfg改名haproxy.cfg.backup
    os.rename('new_haproxy.cfg', 'haproxy.cfg')  # 将new_haproxy.cfg改名为原有haproxy.cfg


def delete(dict_info):
    """

    :param dict_info:
    :return:
    """

if __name__ == '__main__':
    print(u"1.获取记录\n2.添加记录\n3.删除记录\n")  # 获取用户的操作选择
    select_num = input("请输入需要进行的操作编号:")
    if select_num == "1":
        backend = input("请输入backend信息(例如:www.oldboy.org): ")
        get_list = get(backend)
        for i in get_list:
            print("\033[31;1m配置信息如下: %s\033[0m" % i)
    elif select_num == "2":
        print("\033[32;1m请按以下格式输入:\033[0m ")
        print('{"backend":"ttt.oldboy.org","record":{"server":"100.1.7.9","weight":"20","maxconn":"3000"}}')
        read_str = input("\033[30;1m请输入信息>>>\033[0m ")
        data_dict = json.loads(read_str)
        if data_dict == '':
            print("\033[31;1m您输入的内容有误,请重新输入...\033[0m")
        else:
            add(data_dict)
    else:
        print("\033[31;1m您的编号输入错误, 程序退出!!!\033[0m")

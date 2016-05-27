#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import os
import json
from datetime import datetime

FTIME = datetime.now().strftime('%Y%m%d')


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


def json_format():
    """
    : 用于异常捕获
    :return:
    """
    try:
        global DICT_FORMAT
        print("\033[32;1m请按以下格式输入:\033[0m ")
        print('{"backend":"ttt.oldboy.org","record":{"server":"100.1.7.9","weight":"20","maxconn":"3000"}}')
        read_str = input("\033[30;1m请输入需要操作的信息>>>\033[0m ")
        DICT_FORMAT = json.loads(read_str)
    except:
        return False
    else:
        return True


def add(dict_info):
    """
    : 获取backend的名称(变量初始化)
    : 获取backend整个字段(变量初始化)
    : 获取要插入的记录(变量初始化)
    : 只读打开主配置文件,同时以写的方式打开新添加文件
    : 循环读取配置文件同时往新文件里面写,line与backend信息相等,就写入value信息到backend下面
    : 否则直接往文件末尾增加
    :return:
    """
    try:
        backend_name = dict_info.get("backend")
        title_name = "backend %s" % (backend_name)
        record_context = dict_info["record"]
        context_info = "server %s %s weight %s maxconn %s" % (record_context["server"], record_context["server"], record_context["weight"], record_context["maxconn"])
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

        os.rename('haproxy.cfg', 'haproxy.cfg.add.%s' % FTIME)  # 将haproxy.cfg改名haproxy.cfg.backup
        os.rename('new_haproxy.cfg', 'haproxy.cfg')  # 将new_haproxy.cfg改名为原有haproxy.cfg
    except:
        return False
    else:
        return True


def dte(dict_info):
    """
    : 分为两个部分,第一部分用于删除bakend下面的value信息;第二部分用于检测当前backend下面是否为空并且backben的信息与读取内容相等就跳过该信息的写入
    :param dict_info:
    :return:
    """
    try:
        backend_name = dict_info.get("backend")
        record_context = dict_info["record"]
        context_info = "server %s %s weight %s maxconn %s" % (record_context["server"], record_context["server"], record_context["weight"], record_context["maxconn"])
        flag = False
        with open("haproxy.cfg", "r", encoding="utf-8") as obj_read, open("temp_haproxy.cfg", "w", encoding='utf-8') as obj_write:
            for line in obj_read:
                if flag is not True and context_info in line.strip():
                    continue
                else:
                    obj_write.write(line)

        os.rename('haproxy.cfg', 'haproxy.cfg.delete.%s' % FTIME)  # 将haproxy.cfg改名haproxy.cfg.backup
        os.rename('temp_haproxy.cfg', 'haproxy.cfg')  # 将new_haproxy.cfg改名为原有haproxy.cfg

        get_list = get(backend_name)
        with open("haproxy.cfg", "r", encoding="utf-8") as obj_read, open("new_haproxy.cfg", "w", encoding='utf-8') as obj_write:
            for line in obj_read:
                if not get_list and backend_name in line.strip():
                    continue
                else:
                    obj_write.write(line)

        os.rename('new_haproxy.cfg', 'haproxy.cfg')  # 将new_haproxy.cfg改名为原有haproxy.cfg
    except:
        return False
    else:
        return True


def recovery():
    """
    : 进行配置文件版本回退,依据备份记录来做回退操作
    :return:
    """
    print("请输入你要恢复的版本: 1. 执行添加操作之前的版本; 2. 执行删除操作之前的版本")
    in_num = int(input("请输入你要删除的版本编号: "))
    if in_num == 1:
        os.rename('haproxy.cfg.add.%s' % FTIME, 'haproxy.cfg')
        print("\033[34;1m恢复配置文件成功,恢复文件为haproxy.cfg.add.%s\033[0m" % FTIME)
    elif in_num == 2:
        os.rename('haproxy.cfg.delete.%s' % FTIME, 'haproxy.cfg')
        print("\033[34;1m恢复配置文件成功,恢复文件为haproxy.cfg.delete.%s\033[0m" % FTIME)
    else:
        print("\033[31;1mWarning: 输入的编号不存在\033[0m")

if __name__ == '__main__':
    print(u"1.获取记录\n2.添加记录\n3.删除记录\n4.恢复初始配置\n")  # 获取用户的操作选择
    select_num = input("请输入需要进行的操作编号:")
    if select_num == "1":
        backend = input("请输入backend信息(例如:www.oldboy.org): ")
        get_list = get(backend)
        for i in get_list:
            print("\033[31;1m配置信息如下: %s\033[0m" % i)
    elif select_num == "2":
        json_format()
        add_info = add(DICT_FORMAT)
        if add_info:
            print("\033[34;1m添加记录成功\033[0m")
        else:
            print("\033[31;1mWarning: 您输入的内容有误,请重新输入...\033[0m")
    elif select_num == "3":
        json_format()
        delete_info = dte(DICT_FORMAT)
        if delete_info:
            print("\033[34;1m删除记录成功\033[0m")
        else:
            print("\033[31;1mWarning: 您输入的内容有误,请重新输入...\033[0m")
    elif select_num == "4":
        recovery()
    else:
        print("\033[31;1mWarning: 您的编号输入错误, 程序退出!!!\033[0m")

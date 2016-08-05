#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lang

"""
Help:
"""

from conf import auth
from conf import conf
from lib import commons
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def help_msg():
    """
    打印帮助信息
    :return:
    """
    print(commons.color('Available commands:', 32))
    for key in auth.actions:
        print(' ', key)


if __name__ == '__main__':
    argv = sys.argv  # 获取命令行参数列表
    if len(argv) < 2:  # 判断命令行参数数量是否合法
        help_msg()
        exit(1)
    if argv[1] not in auth.actions:  # 判断命令行名命令是否在注册列表中
        commons.err(conf.ERROR_INFO['2001'] % argv[1], quit=True)
    auth.actions[argv[1]](argv[1:])  # 调用注册的对应方法
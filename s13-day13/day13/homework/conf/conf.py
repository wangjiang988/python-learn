#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lang

WELCOME_MSG = '''------------------ Welcome tp login Jumpserver ------------------'''
ERROR_INFO = {
    '1001': '认证失败:错误的用户名或者密码',
    '1002': '尝试太多次数',
    '2001': '命令 [%s] 不存在!',
    '2002': '无效的选项!',
    '3001': '使用错误, Usage(s): %s',
    '4001': '文件 %s 不存在!',
    '5001': '连接失败!',
}
DBS = {"chenliang": "mysql+pymysql://chenliang:123456@172.16.131.129:3306/chenliang",  # 测试环境数据库
       "online": "mysql+pymysql://root:123456@localhost:3306/online",  # 正式环境数据库
       }

DB = DBS['chenliang']
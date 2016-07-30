#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOME_PATH = '%s/home' % BASE_DIR

CODE_LIST = {
    '200': "密码认证OK!",
    '201': "用户名或密码认证失败!",
    '300': "准备发送文件到客户端",
    '301': "客户端准备接收文件数据 ",
    '302': "文件不存在",
    '303': "目录不存在",
    '304': "目标目录不存在",
    '305': "IO 错误",
    '306': "Socket 错误",
    '307': "空间不足",
    "308": "上传成功",
    "309": "上传失败",
    "310": "文件和路径不存在",
    "401": "执行错误",
    "500": "操作执行成功",
}

SERVER_IP = '0.0.0.0'

PORT = 9998

USER_FILE = '../database/userlist'

LOGS = '../logs/ftp_server.log'

DEFAULT_QUOTA = 500

FILE_PER_SIZE = 1024

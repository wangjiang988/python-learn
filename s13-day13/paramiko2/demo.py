#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lang

# 此版本不支持Tab补全, 同时用户名和密码明文

# import paramiko
# import sys
# import os
# import socket
# import select
# import getpass
# # py2.7 应该注释
# from paramiko.py3compat import u
#
# tran = paramiko.Transport(('172.16.131.129', 22,))
# tran.start_client()
# tran.auth_password('root', '123456')
#
# # 打开一个通道
# chan = tran.open_session()
# # 获取一个终端
# chan.get_pty()
# # 激活器
# chan.invoke_shell()
#
# #########
# # 利用sys.stdin,肆意妄为执行操作
# # 用户在终端输入内容，并将内容发送至远程服务器
# # 远程服务器执行命令，并将结果返回
# # 用户终端显示内容
# #########
# while True:
#     # 监视用户输入和服务器返回数据
#     # sys.stdin 处理用户输入
#     # chan 是之前创建的通道，用于接收服务器返回信息
#     readable, writeable, error = select.select([chan, sys.stdin, ], [], [], 1)
#     if chan in readable:
#         try:
#             x = u(chan.recv(1024))
#             # x = chan.recv(1024)  # Python2.7
#             if len(x) == 0:
#                 print('\r\n*** EOF\r\n')
#                 break
#             sys.stdout.write(x)
#             sys.stdout.flush()
#         except socket.timeout:
#             pass
#     if sys.stdin in readable:
#         inp = sys.stdin.readline()
#         chan.sendall(inp)
#
# chan.close()
# tran.close()


import paramiko
import sys
import os
import socket
import select
import getpass
import termios
import tty
# py2.7 应该注释
from paramiko.py3compat import u

# tran = paramiko.Transport(('172.16.131.129', 22,))
# tran.start_client()
# tran.auth_password('root', '123456')

default_username = getpass.getuser()
username = input('Username [%s]: ' % default_username)
if len(username) == 0:
    username = default_username


hostname = input('Hostname: ')
if len(hostname) == 0:
    print('*** Hostname required.')
    sys.exit(1)

tran = paramiko.Transport((hostname, 22,))
tran.start_client()

default_auth = "p"
auth = input('Auth by (p)assword or (r)sa key[%s] ' % default_auth)
if len(auth) == 0:
    auth = default_auth

if auth == 'r':
    default_path = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
    path = input('RSA key [%s]: ' % default_path)
    if len(path) == 0:
        path = default_path
    try:
        key = paramiko.RSAKey.from_private_key_file(path)
    except paramiko.PasswordRequiredException:
        password = getpass.getpass('RSA key password: ')
        key = paramiko.RSAKey.from_private_key_file(path, password)
    tran.auth_publickey(username, key)
else:
    pw = getpass.getpass('Password for %s@%s: ' % (username, hostname))
    tran.auth_password(username, pw)


# 打开一个通道
chan = tran.open_session()
# 获取一个终端
chan.get_pty()
# 激活器
chan.invoke_shell()

#########
# 利用sys.stdin,肆意妄为执行操作
# 用户在终端输入内容，并将内容发送至远程服务器
# 远程服务器执行命令，并将结果返回
# 用户终端显示内容
#########

# 获取原tty属性
oldtty = termios.tcgetattr(sys.stdin)

try:
    # 为tty设置新属性
    # 默认当前tty设备属性：
    #   输入一行回车，执行
    #   CTRL+C 进程退出，遇到特殊字符，特殊处理。

    # 这是为原始模式，不认识所有特殊符号
    # 放置特殊字符应用在当前终端，如此设置，将所有的用户输入均发送到远程服务器
    tty.setraw(sys.stdin.fileno())
    chan.settimeout(0.0)

    while True:
        # 监视 用户输入 和 远程服务器返回数据（socket）
        # 阻塞，直到句柄可读
        r, w, e = select.select([chan, sys.stdin], [], [], 1)
        if chan in r:
            try:
                x = u(chan.recv(1024))
                if len(x) == 0:
                    print('\r\n*** EOF\r\n')
                    break
                sys.stdout.write(x)
                sys.stdout.flush()
            except socket.timeout:
                pass
        if sys.stdin in r:
            x = sys.stdin.read(1)
            if len(x) == 0:
                break
            chan.send(x)

finally:
    # 重新设置终端属性
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

chan.close()
tran.close()
#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang



# import paramiko
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='172.16.131.129', port=22, username='chenliang', password='00d50c21639')
#
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('free -g')
# # 获取命令结果
# result = stdout.read()
# print(result)
#
# # 关闭连接
# ssh.close()


# import paramiko
#
# transport = paramiko.Transport(('172.12.131.34', 22))
# transport.connect(username='chenliang', password='b54d00d50c21639')
#
# ssh = paramiko.SSHClient()
# ssh._transport = transport
#
# stdin, stdout, stderr = ssh.exec_command('df')
# print(stdout.read())
#
# transport.close()

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/chenliang/.ssh/id_rsa')

transport = paramiko.Transport(('172.16.131.129', 22))
transport.connect(username='chenliang', pkey=private_key)

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')

transport.close()
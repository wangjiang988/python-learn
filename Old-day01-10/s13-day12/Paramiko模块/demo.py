#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lazar

import paramiko
import uuid


class SSHConnection(object):
    def __init__(self, host='', port=22, username='', pwd='639'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None

    def create_file(self):
        file_name = str(uuid.uuid4())
        with open(file_name, 'w') as f:
            f.write('sb')
        return file_name

    def run(self):
        self.connect()
        self.upload('/home/chenliang/demo.py')
        self.rename('/home/chenliang/demo.py', '/home/chenliang/new.py')
        self.close()

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def upload(self, target_path):
        # 连接，上传
        file_name = self.create_file()

        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/demo.py
        sftp.put(file_name, target_path)

    def rename(self, old_path, new_path):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        cmd = "mv %s %s" % (old_path, new_path,)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 获取命令结果
        result = stdout.read()

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        stdin.close()
        # 获取命令结果
        reslut = stdout.read().splitlines()
        for line in reslut:
            if line:
                print(line)


demo = SSHConnection()
while True:
    ret = input(">> ")
    demo.connect()
    demo.cmd(ret)
    demo.close()

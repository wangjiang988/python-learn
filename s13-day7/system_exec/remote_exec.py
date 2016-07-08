#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.108', 22, 'test', '123')
stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())
ssh.close();


import paramiko

private_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('主机名 ', 端口, '用户名', key)

stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())
ssh.close()


import os,sys
import paramiko

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='test',password='123')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test.py','/tmp/test.py')
t.close()


import os,sys
import paramiko

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='test',password='123')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test.py','/tmp/test2.py')
t.close()


import paramiko

pravie_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pravie_key_path)

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='test',pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test3.py','/tmp/test3.py')

t.close()

import paramiko

pravie_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pravie_key_path)

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='test',pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test3.py','/tmp/test4.py')

t.close()
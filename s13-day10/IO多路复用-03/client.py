#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import socket

ip_port = ('127.0.0.1', 9999,)
sk = socket.socket()
sk.connect(ip_port)

recv_bytes = sk.recv(1024)
recv_str = str(recv_bytes, encoding='utf-8')

while True:
    inp = input(">> ")
    if inp == 'q':
        break
    sk.sendall(bytes(inp, encoding='utf-8'))
    print(str(sk.recv(1024), encoding='utf-8'))


# 如何通过IO多路复用实现一个多并发


import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9999,))
data = sk.recv(1024)
print(data)

while True:
    inp = input('>> ')
    if inp == 'quit':
        break
    sk.sendall(bytes(inp, encoding='utf-8'))
    print(sk.recv(1024))
sk.close()


# 伪并发读写分离实现
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9999,))
data = sk.recv(1024)
print(data)

while True:
    inp = input('>> ')
    if inp == 'quit':
        break
    sk.sendall(bytes(inp, encoding='utf-8'))
    print(sk.recv(1024))
sk.close()
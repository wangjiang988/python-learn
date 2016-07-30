#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# Socket Server

import socket

ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('server waiting...')
    conn, addr = sk.accept()

    client_data = conn.recv(1024)
    print(client_data)
    conn.sendall('不要回答,不要回答,不要回答')

    conn.close()

# Socket Client

import socket
ip_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall('请求占领地球')

server_reply = sk.recv(1024)
print(server_reply)

sk.close()
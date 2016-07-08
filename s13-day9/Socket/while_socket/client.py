#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
import socket
ip_port = ('127.0.0.1', 9999)

# 准备状态
s = socket.socket()

# 拨号
s.connect(ip_port)

while True:
    # 发送消息
    send_data = input(">>: ").strip()
    if len(send_data) == 0:
        continue
    s.send(bytes(send_data, encoding='utf8'))
    if send_data == 'exit':
        break

    # 接收消息
    recv_data = s.recv(1024)
    print(str(recv_data, encoding='utf8'))

# 结束通话
s.close()

#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import socket

# 定义IP加端口
ip_port = ('127.0.0.1', 9999)  # 一定是元组形式

# 买通信设备
s = socket.socket()

# 关联通信设备
s.bind(ip_port)

# 开机
s.listen(5)  # 最大挂起5个连接, 3.0默认为128

# 待机
conn, addr = s.accept()  # 通信连接

while True:
    try:
        # 接收消息
        recv_data = conn.recv(1024)  # 接收1024字节
        if str(recv_data, encoding='utf-8') == 'exit':
            break
        # 发送消息
        send_data = recv_data.upper()
        conn.send(send_data)
    except Exception:
        break

# 结束通话
conn.close()

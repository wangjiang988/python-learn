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
s.listen(1)  # 最大挂起5个连接, 3.0默认为128

while True:
    # 待机 # 通信连接
    conn, addr = s.accept()

    while True:
        # 接收消息
        try:  # 代表当前conn无效,本次链接结束
            recv_data = conn.recv(1024)  # 接收1024字节
            if len(recv_data) == 0:
                break
            # 发送消息
            send_data = recv_data.upper()
            print(send_data)

            conn.send(send_data)
        except Exception:
            break

    # 结束通话
    conn.close()

#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
import socket
ip_port = ('127.0.0.1', 9999)

# 准备状态
s = socket.socket()

# 拨号
s.connect(ip_port)  # 连接服务端, 如果服务端已经存在一个正常链接, 那么挂起

while True:  # 基于connect建立的链接来循环发送消息
    # 发送消息
    send_data = input(">>: ").strip()
    if send_data == 'exit':
        break
    if len(send_data) == 0:  # 如果输入为空, 则继续输入
        continue
    s.send(bytes(send_data, encoding='utf8'))

    # 接收消息, 解决粘包问题
    ready_tag = s.recv(1024)  # 接收长度
    ready_tag = str(ready_tag, encoding='utf8')
    if ready_tag.startswith('Ready'):
        msg_size = int(ready_tag.split('|')[-1])  # 获取待接收数据长度
    start_tag = "Start"
    s.send(bytes(start_tag, encoding='utf8'))  # 客户端发送确认信息

    # 基于已经收到的待接收数据长度,循环接收数据
    recv_size = 0  # 初始大小
    recv_msg = b''  # 初始字节

    while recv_size < msg_size:  # 当接收大小小于获取的待接收数据长度, 做字符串拼接
        recv_data = s.recv(1024)
        recv_msg += recv_data  # 字节数累加
        recv_size += len(recv_data)  # 接收大小累加
        print("MSG SIZE %s RECE DATA %s" % (msg_size, recv_size))  # 打印MSG大小,接收大小
    print(str(recv_msg, encoding='utf8'))

# 结束通话
s.close()

#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import socket
import subprocess  # 执行命令模块

# 定义IP加端口
ip_port = ('127.0.0.1', 9999)  # 定义元组, 必须是元组形式

# 买通信设备
s = socket.socket()  # 绑定协议,生成套接字

# 关联通信设备
s.bind(ip_port)  # 绑定ip+端口+协议,用来唯一标识一个进程

# 开机
s.listen(1)  # 最大挂起链接数, 3.0默认为128

while True: # 重复接收新的连接信息
    # 待机 # 通信连接
    conn, addr = s.accept()  # 接收客户端的链接请求, 返回conn(相当于特定的链接),addr(客户端的ip和端口)

    while True:  # 用来定义一个链接重复收发消息
        # 接收消息
        try:  # 代表当前conn无效,本次链接结束, 捕捉客户端异常关闭
            recv_data = conn.recv(1024)  # 接收1024字节, 阻塞
            if len(recv_data) == 0:  # 客户端如果退出, 服务端将收到空消息, 退出
                break

            # 发送消息
            p = subprocess.Popen(str(recv_data, encoding='utf8'), shell=True, stdout=subprocess.PIPE)  # 执行系统命令, windows平台命令的标准输出是gbk编码,需要转化
            res = p.stdout.read()  # 获取标准输出
            if len(res) == 0:  # 执行错误命令, 标准输出为空
                send_data = "input wrong: %s" % str(recv_data, encoding='utf8')
            else:
                send_data = str(res, encoding='gbk')  # 命令执行OK, 字节gbk-str-utf8
            # print(send_data)
            send_data = bytes(send_data, encoding='utf8')  # 转换编码

            # Socket Server解决粘包问题
            ready_tag = "Ready|%s" % len(send_data)  # 发送长度
            conn.send(bytes(ready_tag, encoding='utf8'))
            feedback = conn.recv(1024)  # 返回值, 接收确认信息
            feedback = str(feedback, encoding='utf8')

            if feedback.startswith('Start'):
                conn.send(send_data)  # 发送命令的执行结果
        except Exception:
            break

    # 结束通话
    conn.close()

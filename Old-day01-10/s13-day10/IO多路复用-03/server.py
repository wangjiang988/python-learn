#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9999,))
sk.listen(5)

while True:
    conn, addr = sk.accept()
    conn.sendall(bytes('test', encoding='utf-8'))

    while True:
        recv_bytes = conn.recv(1024)
        if str(recv_bytes, encoding='utf-8') == 'q':
            break
        conn.sendall(recv_bytes)

# 如何通过IO多路复用实现一个多并发 , IO操作不占用CPU, IO多路复用用于管理多个IO操作


# 概述: 用来监听socket对象内部是否发生变化?
#    - 什么时候变化, 连接或着收发消息
#    服务器端的socket对象发生变化, 就表示有新的连接
    # sk 接收客户端连接, 新连接来了
    # conn 有新消息来了
# select, poll, epoll

# 伪并发实现
import socket
import select
import time

sk = socket.socket()
sk.bind(('127.0.0.1', 9999,))
sk.listen(5)

inputs = [sk, ]
while True:
    rlist, w, e, = select.select(inputs, [], [], 1)
    print(time.time())
    print(len(inputs), len(rlist))
    print(rlist)
    # 监听sk(服务端)对象,如果sk对象发生变化,表示有客户端来连接了, 此时rlist为[sk]
    # 监听conn对象,如果conn发生变化,表示客户端有新消息发送过来, 此时rlist为[客户端]
    # inputs里面有什么rlist里面就有什么, 处理连接信息
    for r in rlist:  # 伪并发操作
        if r == sk:  # 表示新客户端连接
            conn, addr = r.accept()
            # conn其实也是socket对象
            inputs.append(conn)
            conn.sendall(bytes('test', encoding='utf-8'))
        else:
            # 有人发送消息了
            try:  # 抛出异常, 自动断开连接
                ret = r.recv(1024)
                r.sendall(ret)  # 可以这样写, 推荐读写分离模式
                if not ret:
                    raise Exception('Close connection')
            except Exception as e:
                inputs.remove(r)  # 当客户端断开之后就移除
# rlist = [sk] # 有连接就返回sk, socket对象列表
# rlist = [] # 没有连接返回空
# [sk, ] # 监听服务端socket是否有变化
# 1为等待时间1s


# 伪并发读写分离实现
import socket
import select
import time

sk = socket.socket()
sk.bind(('127.0.0.1', 9999,))
sk.listen(5)

inputs = [sk, ]
outputs = []
while True:
    rlist, wlist, e, = select.select(inputs, outputs, [], 1)
    print(time.time())
    print(len(inputs), len(rlist), len(wlist))
    print(rlist)
    # 监听sk(服务端)对象,如果sk对象发生变化,表示有客户端来连接了, 此时rlist为[sk]
    # 监听conn对象,如果conn发生变化,表示客户端有新消息发送过来, 此时rlist为[客户端]
    # outpus里面有什么wlist就有什么, 处理消息发送
    for r in rlist:  # 伪并发操作
        if r == sk:  # 表示新客户端连接
            conn, addr = r.accept()
            # conn其实也是socket对象
            inputs.append(conn)
            conn.sendall(bytes('test', encoding='utf-8'))
        else:
            # 有人发送消息了
            try:  # 抛出异常, 自动断开连接
                ret = r.recv(1024)
                # r.sendall(ret)  # 可以这样写, 推荐读写分离模式
                if not ret:
                    raise Exception('Close connection')
                else:
                    outputs.append(r)
            except Exception as e:
                inputs.remove(r)

    for w in wlist:  # 表示所有给我发过消息的人
        w.sendall(bytes('response 200', encoding='utf-8'))
        outputs.remove(w)  # 表示回过消息, 下次不用再回复, 当回过消息后就移除


# 伪并发读写分离及消息合并实现
import socket
import select
import time

sk = socket.socket()
sk.bind(('127.0.0.1', 9999,))
sk.listen(5)

inputs = [sk, ]
outputs = []  # 定义空列表
messages = {}  # 定义信息字典
# messages = {
# conn1: [message1, message2, ...]
# conn2: [message1, message2, ...]
# }
while True:
    rlist, wlist, elist, = select.select(inputs, outputs, [], 1)
    print(time.time())
    print(len(inputs), len(rlist), len(wlist))
    print(rlist)
    # 监听sk(服务端)对象,如果sk对象发生变化,表示有客户端来连接了, 此时rlist为[sk]
    # 监听conn对象,如果conn发生变化,表示客户端有新消息发送过来, 此时rlist为[客户端]
    # outpus里面有什么wlist就有什么, 处理消息发送
    for r in rlist:  # 伪并发操作
        if r == sk:  # 表示新客户端连接
            conn, addr = r.accept()
            # conn其实也是socket对象
            inputs.append(conn)
            messages[conn] = []  # 专门用于存放消息
            conn.sendall(bytes('test', encoding='utf-8'))
        else:
            # 有人发送消息了
            try:  # 抛出异常, 自动断开连接
                ret = r.recv(1024)
                # r.sendall(ret)  # 可以这样写, 推荐读写分离模式
                if not ret:
                    raise Exception('Close connection')
                else:
                    outputs.append(r)
                    messages[r].append(ret)
            except Exception as e:
                inputs.remove(r)
                del messages[r]  # 存储消息清空

    for w in wlist:  # 表示所有给我发过消息的人
        msg = messages[w].pop()  # 上一次发送的消息
        resp = msg + bytes('response 200', encoding='utf-8')  # 将发送和接收消息拼接
        w.sendall(resp)
        outputs.remove(w)  # 表示回过消息, 下次不用再回复, 当回过消息后就移除



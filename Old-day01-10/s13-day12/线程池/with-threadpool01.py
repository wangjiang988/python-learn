#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 通过加入contextlib.contextmanager装饰器,就可以执行with上下文管理

import contextlib

@contextlib.contextmanager
def worker_state(state_list, worker_thread):
    """
    用于记录线程中正在等待的线程数
    """
    state_list.append(worker_thread)
    try:
        yield
    finally:
        state_list.remove(worker_thread)

free_list = []
current_thread = 'alex'

with worker_state(free_list, current_thread):
    print(123)
    print(456)


# 通过上下文管理, 我们可以应用到sock中, 退出是自动关闭socket连接

import contextlib
import socket

@contextlib.contextmanager
def context_socket(host, port):
    """
    用于记录线程中正在等待的线程数
    """
    sk = socket.socket()
    sk.bind((host, port))
    sk.listen(5)
    try:
        yield sk
    finally:
        sk.close()

with context_socket('127.0.0.1', 8888) as sock:
    print(sock)

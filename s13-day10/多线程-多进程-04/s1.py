#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
import time


def f1(args):
    time.sleep(5)
    print(args)


# f1('1')

# 单进程, 单线程
"""
1, 一个应用程序, 可以有多进程和多线程
2, 默认: 单进程, 单线程
3, 单进程, 多线程, 性能不会有提升
    多线程: IO操作不会占用CPU, 多线程提高并发
    多进程: 计算性操作用到CPU, 多进程提高并发
4, GIL, 全局解释器锁
    - IO密集型用多线程, 计算密集型的用多进程
"""


# 多线程
import threading

t = threading.Thread(target=f1, args=(123, ))  # 创建线程
t.setDaemon(True)  # true表示主线程不等此子线程
t.start()  # 并不代表当前线程会被立即执行, 而是由CPU调度
t.join(2)  # 表示主线程到此, 等待...直到子线程执行完毕, 参数表示最多等2s
f1(111)
print('end')
print('end')
print('end')


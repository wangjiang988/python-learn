#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import threading
import time

NUM = 10


def func(l):
    global NUM
    # lock
    l.acquire()
    NUM -= 1
#    l.acquire()  # 多层锁
    time.sleep(2)
#    l.release()
    print(NUM)
    # unlock
    l.release()

lock = threading.Lock()  # 单次锁, 不支持多重锁
# lock = threading.RLock()  # 多次锁, 支持多重嵌套


for i in range(10):  # 线程同时操作会产生脏数据
    t = threading.Thread(target=func, args=(lock, ))
    t.start()


# 信号量
"""
互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去。
"""

import threading
import time

NUM = 10


def func(j, l):
    global NUM
    # lock
    l.acquire()  # 30, 5 .. 25 ; 5 ... 20 ...
    NUM -= 1
    time.sleep(2)
    print(NUM, j)
    # unlock
    l.release()

lock = threading.BoundedSemaphore(5)  # 锁, 做多允许5个线程同时运行

for i in range(30):  # 线程同时操作会产生脏数据
    t = threading.Thread(target=func, args=(i, lock, ))
    t.start()


# event
"""
python线程的事件用于主线程控制其他线程的执行，事件主要提供了三个方法 set、wait、clear。

事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞。

clear：将“Flag”设置为False
set：将“Flag”设置为True
"""

import threading


def func(j, e):
    print(j)
    e.wait()  # 检测当前是什么灯, 如果是红灯, 停; 如果是绿灯, 行; 默认为红灯
    print(j + 100)

event = threading.Event()

for i in range(10):
    t = threading.Thread(target=func, args=(i, event, ))
    t.start()

# ===============

event.clear()  # 主动设置成红灯
inp = input(">> ")
if inp == "1":
    event.set()  # 主动设置成绿灯, wait不等待


# 条件（Condition）

"""
使得线程等待, 只有满足某条件时, 才释放n个线程
"""

# example 1
import threading


def func(j, conn):
    print(j)  # 10个线程同时print
    conn.acquire()
    conn.wait()
    print(j + 100)
    conn.release()

c = threading.Condition()

for i in range(10):
    t = threading.Thread(target=func, args=(i, c, ))
    t.start()

while True:
    inp = input(">> ")  # 主线程等待, 输入多少放出多少
    if inp == "q":
        break
    # 下面为固定用法
    c.acquire()
    c.notify(int(inp))
    c.release()


# example 2
import threading


def condition():  # 当条件满足之后放行
    ret = False
    r = input(">> ")
    if r == "true":
        ret = True
    else:
        ret = False
    return ret


def func(j, conn):
    print(j)  # 10个线程同时print
    conn.acquire()
    conn.wait_for()
    print(j + 100)
    conn.release()

c = threading.Condition()

for i in range(10):
    t = threading.Thread(target=func, args=(i, c, ))
    t.start()


# Timer
"""
定时器, 指定n秒后执行操作
"""

from threading import Timer


def hello():
    print("hello, world")

t = Timer(1, hello)
t.start()  # after 1 seconds, "hello, world" will be printed


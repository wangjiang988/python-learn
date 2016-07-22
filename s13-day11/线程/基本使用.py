#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


# 创建线程方式, 最常用的

import threading


def f1(args):
    print(args)

t = threading.Thread(target=f1, args=(123, ))
t.start()  # 创建线程, 等待调度
t.run()  # f1由run方法调用


# 创建线程方式, 自定义类

import threading


class MyThread(threading.Thread):
    def __init__(self, func, args):
        self.func = func
        self.args = args
        super(MyThread, self).__init__()

    def run(self):
        self.func(self.args)


def f2(args):
    print(args)

obj = MyThread(f2, 123)
obj.start()  # 调用run方法

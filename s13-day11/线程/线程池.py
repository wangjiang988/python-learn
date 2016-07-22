#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 线程池
"""

"""

import queue
import threading
import time


class ThreadPool:
    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self._q = queue.Queue(maxsize)

        for i in range(maxsize):
            self._q.put(threading.Thread)  # 单个单个的类名

    def get_thread(self):  # 定义线程池获取函数
        return self._q.get()

    def add_thread(self):  # 定义线程池添加函数
        self._q.put(threading.Thread)

pool = ThreadPool(5)


def task(args, p):
    print(args)
    time.sleep(10)
    p.add_thread()  # 手动增加线程池

for j in range(100):
    # t等于threading.Thread类
    t = pool.get_thread()  # 获取线程池
    obj = t(target=task, args=(j, pool, ))
    obj.start()
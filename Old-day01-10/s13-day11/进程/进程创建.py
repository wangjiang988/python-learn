#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 多进程创建

# from multiprocessing import Process
#
#
# def foo(j):
#     print('say hi', j)
#
#
# for i in range(10):
#     p = Process(target=foo, args=(i,))
#     p.start()

# from multiprocessing import Process, Array
#
# templates = Array('i', [11, 22, 33, 44])
#
#
# def Foo(i):
#     templates[i] = 100 + i
#     for item in templates:
#         print(i, '----->', item)
#
#
# for i in range(2):
#     p = Process(target=Foo, args=(i,))
#     p.start()


# 进程数据共享

# from multiprocessing import Process, queues
# import multiprocessing
#
#
# def Foo(i, args):
#     args.put(i)
#     print('say hi', i, args.qsize())
#
# li = queues.Queue(20, ctx=multiprocessing)
#
# for i in range(10):
#     p = Process(target=Foo, args=(i, li, ))
#     p.start()


from multiprocessing import Process,Manager

obj = Manager()
dic = obj.dict()


def Foo(j):
    dic[j] = 100 + j
    print(dic.values())

for i in range(3):
    p = Process(target=Foo,args=(i, ))
    p.start()
    p.join()
# import time
# time.sleep(0.1)

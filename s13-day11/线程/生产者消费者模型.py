#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
# 生产者消费者模型创建

import threading
import queue
import time

# 创建队列, 最大容量20
q = queue.Queue(20)


def productor(args):
    """
    ;买票
    :param args:
    :return:
    """
    while True:  # 一直创建购票订单, 创建满后进行阻塞
        q.put(str(args) + ' 号票务' + ' - 生产订单')


for i in range(300):  # 300个访问人数
    t = threading.Thread(target=productor, args=(i, ))
    t.start()


def consumer(args):
    """
    ;服务器后台
    :param args:
    :return:
    """
    while True:
        print('消费者 %s号' % args, q.get())
        time.sleep(2)

for j in range(20):  # 20台服务器进行处理
    t = threading.Thread(target=consumer, args=(j, ))
    t.start()
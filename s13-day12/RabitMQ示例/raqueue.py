#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import queue
import threading


message = queue.Queue(10)


def producer(args):
    while True:
        message.put(args)


def consumer(args):
    while True:
        msg = message.get()
        print(msg)


for i in range(12):
    t = threading.Thread(target=producer, args=(i, ))
    t.start()

for j in range(10):
    t = threading.Thread(target=consumer, args=(j, ))
    t.start()
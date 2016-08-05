#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')

# 带参数发送
"""
python3 mq发布订阅-发布者.py 'welcome to beijing!!!'
 [x] Sent 'welcome to beijing!!!'
"""
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()
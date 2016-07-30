#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

# 使用exchange的direct
channel.exchange_declare(exchange='topic_logs', type='topic')


routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()

"""
# 运行结果
python3 mq模糊匹配-生产者.py 'c.orange.info' 'testinfo'
 [x] Sent 'c.orange.info':'testinfo'
"""
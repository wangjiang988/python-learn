#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

# 使用exchange的direct
channel.exchange_declare(exchange='direct_logs', type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()

"""
# 运行结果
python3 mq关键字发送-生产者.py warning chenliang
 [x] Sent 'warning':'chenliang'


python3 mq关键字发送-生产者.py warning testmessage
 [x] Sent 'warning':'testmessage'
"""
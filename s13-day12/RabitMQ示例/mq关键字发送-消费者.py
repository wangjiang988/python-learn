#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', type='direct')

# 随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

# 根据用户输入进行绑定
for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()

"""
# 运行结果
python3 mq关键字发送-消费者.py info
 [*] Waiting for logs. To exit press CTRL+C
 [x] 'info':b'Hello World!'

python3 mq关键字发送-消费者.py warning
 [*] Waiting for logs. To exit press CTRL+C
 [x] 'warning':b'chenliang'

python3 mq关键字发送-消费者.py warning error
 [*] Waiting for logs. To exit press CTRL+C
 [x] 'warning':b'testmessage'

python3 mq关键字发送-消费者.py info warning
 [*] Waiting for logs. To exit press CTRL+C
 [x] 'warning':b'testmessage'
"""
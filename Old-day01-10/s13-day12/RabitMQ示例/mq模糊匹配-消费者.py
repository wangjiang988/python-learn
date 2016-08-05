#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

"""

exchange type = topic

在topic类型下，可以让队列绑定几个模糊的关键字，之后发送者将数据发送到exchange，exchange将传入”路由值“和 ”关键字“进行匹配，匹配成功，则将数据发送到指定队列。

# 表示可以匹配 0 个 或 多个 单词
*  表示只能匹配 一个 单词

发送者路由值              队列中
old.boy.python          old.*  -- 不匹配
old.boy.python          old.#  -- 匹配
"""

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', type='topic')

# 随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

# 根据用户输入进行绑定
for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()

"""
# 运行结果
python3 mq模糊匹配-消费者.py '*.orange.*'
 [*] Waiting for logs. To exit press CTRL+C
 [x] 'c.orange.info':b'testinfo'
"""
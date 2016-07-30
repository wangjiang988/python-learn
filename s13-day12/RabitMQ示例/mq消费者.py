#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 基本消息队列, 接收端

import pika

# ########################## 消费者 ##########################

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


# 消息不丢失, 针对取数据端
"""
acknowledgment 消息不丢失
no-ack ＝ False，如果消费者遇到情况(its channel is closed, connection is closed, or TCP connection is lost)挂掉了，那么，RabbitMQ会重新将该任务添加到队列中。
"""
import pika

# ########################## 消费者 ##########################

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    import time
    time.sleep(10)
    print('Ok')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback, queue='hello', no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


# durable 消息不丢失
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='hello', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    import time
    time.sleep(10)
    print('Ok')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback, queue='hello', no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# 消息获取按顺序获取

"""
默认消息队列里的数据是按照顺序被消费者拿走，例如：消费者1 去队列中获取 奇数 序列的任务，消费者1去队列中获取 偶数 序列的任务。
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    import time
    time.sleep(10)
    print('Ok')
    ch.basic_ack(delivery_tag=method.delivery_tag)

# channel.basic_qos(prefetch_count=1) 表示谁来谁取，不再按照奇偶数排列
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='hello', no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

"""
发布订阅和简单的消息队列区别在于，发布订阅会将消息发送给所有的订阅者，而消息队列中的数据被消费一次便消失。所以，RabbitMQ实现发布和订阅时，会为每一个订阅者创建一个队列，而发布者发布消息时，会将消息放置在所有相关队列中。
exchange type = fanout
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

# 创建频道logs, 类型为exchange type = fanout
channel.exchange_declare(exchange='logs', type='fanout')

# 随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 绑定队列信息
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()
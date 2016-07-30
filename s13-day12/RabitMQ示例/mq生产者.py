#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 基本消息队列, 发送端

import pika

# ######################### 生产者 #########################

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()

# durable 消息不丢失, 针对服务端做消息持久化

import pika

# ######################### 生产者 #########################

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='hello', durable=True)

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!', properties=pika.BasicProperties(
    delivery_mode=2  # make message persistent
))

print(" [x] Sent 'Hello World!'")
connection.close()

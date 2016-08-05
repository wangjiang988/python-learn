#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lazar

"""
; 当客户端启动时，它创建了匿名的exclusive callback queue.
; 客户端的RPC请求时将同时设置两个properties： reply_to设置为 callback queue； correlation_id 设置为每个request一个独一无二的值.
; 请求将被发送到an rpc_queue queue.
; RPC端或者说server一直在等待那个queue的请求。当请求到达时，它将通过在reply_to指定的queue回复一个message给client。
; client一直等待callback queue的数据。当message到达时，它将检查 correlation_id 的值，如果值和它request发送时的一致那么就将返回响应。
"""

import pika

# 建立一个连接并定义一个队列
connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))

channel = connection.channel()

# 队列持久化
channel.queue_declare(queue='rpc_queue', durable=True)


# 定义斐波纳契函数，假定输入的都是合法正数
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 定义回调的basic_consume, RPC服务的核心。当收到请求后执行这个函数并返回结果
def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 有时候可能会执行多个服务端，为了在多个服务端上均匀的分布负荷，需要定义prefetch_count
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()

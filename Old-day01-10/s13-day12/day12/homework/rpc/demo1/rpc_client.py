#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lazar

import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        # 建立一个连接,通道并定义一个专门的'callback'队列来接收回复
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.16.131.129'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        # 订阅'callback'对列,接收RPC返回结果
        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

    # 'on_response' 在每个返回中执行的回调是一个简单的任务,对每个返回消息将检查是否correlation_id是我们需要查找的那个ID,如果是就将结果保存到self.response并终端consuming循环
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        """
        ; 定义main方法-用来执行实际的RPC请求
        ; 当前方法中,我们首先生产一个唯一的correlation_id号并保存,'on_response'回调函数将用改号码来匹配发送和接收的消息值
        ; 发送请求信息,使用reply_to和correlation_id两个属性
        ; 等待返回结果,并将结果返回给用户
        :param n:
        :return:
        """
        self.response = None
        # 生成一个随机字符串
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='', routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to=self.callback_queue,
                                                                   correlation_id=self.corr_id, ), body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)

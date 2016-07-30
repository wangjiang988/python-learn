#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import queue

# 先进先出队列
# put放数据, 是否阻塞, 阻塞时的超时时间
# get取数据

q = queue.Queue(10)  # 表示队列最大长度
q.put(11)
q.put(22)

# q.put(33, block=False, timeout=2)  # block=False表示不再阻塞, timeout表示超时时间

# print(q.qsize())  # 队列里面的真实个数
# print(q.get())

# get获取数据的时候, 默认阻塞, block=False表示不阻塞, timeout超时时间
print(q.get(block=False, timeout=2))
print(q.get())
print(q.get())  # 执行的时候会阻塞
print(q.get(block=False, timeout=2))  # 执行的时候直接报错

print(q.empty())  # 判断是否为空
print(q.full())  # 判断队列是否满了
print(q.maxsize)  # 获取最大个数
q.task_done()  # 任务取出完成
q.join()  # join和task_donw配合使用, 阻塞进程, 当队列中任务执行完毕之后, 不再阻塞

# queue.LifoQueue  后队进先出队列
q = queue.LifoQueue()
q.put(123)
q.put(456)
print(q.get())

# queue.PriorityQueue 优先级队列
q = queue.PriorityQueue()
q.put((1, "alex1"))
q.put((1, "alex2"))
q.put((1, "alex3"))
q.put((3, "alex3"))
print(q.get())

# queue.deque 双向对队
q = queue.deque()
q.append(123)
q.append(333)
q.appendleft(456)
q.pop()
q.popleft()

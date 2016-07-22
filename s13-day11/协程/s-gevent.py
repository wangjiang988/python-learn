#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# greenlet
#
# from greenlet import greenlet
#
#
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()

#
# import gevent
#
#
# def foo():
#     print('Running in foo')
#     gevent.sleep(0)
#     print('Explicit context switch to foo again')
#
#
# def bar():
#     print('Explicit context to bar')
#     gevent.sleep(0)
#     print('Implicit context switch back to bar')
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

# http请求发送

from gevent import monkey
monkey.patch_all()
import gevent
import requests


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.bdp.cn/'),
    gevent.spawn(f, 'http://www.51cto.com/'),
    gevent.spawn(f, 'http://www.500.com/'),
])

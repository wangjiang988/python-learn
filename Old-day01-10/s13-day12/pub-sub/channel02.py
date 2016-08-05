#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 定义一个RedisHelper类, 供发布和订阅单独调用

import redis


class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='172.16.131.129', port=6379)

    def public(self, msg, chan):
        self.__conn.publish(chan, msg)
        return True

    def subscribe(self, chan):
        pub = self.__conn.pubsub()
        pub.subscribe(chan)
        pub.parse_response()
        return pub
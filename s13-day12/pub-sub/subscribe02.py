#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import channel02

obj = channel02.RedisHelper()
data = obj.subscribe('fm103.7')

while True:
    print(data.parse_response())
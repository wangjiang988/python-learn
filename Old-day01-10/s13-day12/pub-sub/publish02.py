#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import channel02

obj = channel02.RedisHelper()

while True:
    inp = input('>> ')
    if inp == '':
        print("当前输入为空, 请重新输入...")
        continue
    else:
        obj.public(inp, 'fm103.7')
#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

count = 0
while True:
    count += 1
    if 50 < count < 60:
        # if count > 50 and count < 60:
        continue
    print(u"{0:03d} 您是风儿,我是沙...".format(count))
    if 100 == count:
        print("Fuck,Gun...")
        break

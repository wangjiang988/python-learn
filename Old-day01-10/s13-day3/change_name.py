#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
with open("db1", "r", encoding='utf-8') as f1, open("db2", "w", encoding='utf-8') as f2:
    for line in f1:
        new_str = line.replace("admin", "eric")
        f2.write(new_str)
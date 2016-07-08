#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 对象是基于类创建, pickle, load: 切记, 一定要先导入相关类
import pickle
from s1 import Foo


ret = pickle.load(open('db', 'rb'))

print(ret)
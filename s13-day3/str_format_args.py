#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 通过字符串格式化来应用函数参数* 和 **

s1 = "I am {0}, age {1}".format("alex", 18)  # {}代表占位符
print(s1)
s2 = "I am {0}, age {1}".format(*["alex", 18])  # {}代表占位符
print(s2)

s3 = "I am {name}, age {age}".format(name="alex", age=18)  # {}代表占位符
print(s3)

dic = {'name': 'alex', 'age': 18}
s4 = "I am {name}, age {age}".format(**dic)  # {}代表占位符
print(s4)
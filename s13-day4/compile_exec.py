#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# compile 用于编译,将字符串编译为python代码
s = "print(123)"

# 编译,single(单行python程序),eval(表达式),exec(python原有模式)
# compile 将字符串编译为python代码,exec需要加双引号
r = compile(s, "<string>", "exec")
# 执行python代码
exec(r)

# eval 执行处理表达式,有返回值
#
s = "8*8"
ret = eval(s)
print(ret)

# exec 执行python代码活着字符串,没有返回值
# 接收为字符串或者代码
exec("6+7+8")
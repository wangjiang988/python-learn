#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


import logging

# create logger
logger = logging.getLogger('TEST-LOG')  # 哪个程序发的日志,首先获取到logger对象
logger.setLevel(logging.DEBUG)  # 设定一个全局的日志级别

# create console handler and set level to debug
ch = logging.StreamHandler()  # 将日志打印到屏幕
ch.setLevel(logging.DEBUG)  # 打印到屏幕的日志级别

# create file handler and set level to warning
fh = logging.FileHandler("access.log")  # 将日志打印到文件
fh.setLevel(logging.WARNING)  # WARNING及更高的日志输出出到文件
# create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(filename)s - %(module)s - %(process)d - %(lineno)d - %(levelname)s - %(message)s')

# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch and fh to logger
logger.addHandler(ch)  # 把日志打印到指定的handler里面
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

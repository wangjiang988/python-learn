#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import math
import re

integers_regex = re.compile(r'\b[\d\.]+\b')


def calc(expression, advanced=False):
    # 将转换后的表达式通过eval来计算
    """
    # 将字符串str当成有效的表达式来求值并返回计算结果。
    :param expression:
    :param advanced:
    :return:
    """
    def safe_eval(expression, symbols={}):
        try:
            eval(expression, dict(__builtins__=None), symbols)
        except:
            return "表达式输入错误..."
        else:
            return eval(expression, dict(__builtins__=None), symbols)

    # 将表达式中的所有数值转换为浮点数
    def number_to_float(match):
        # 返回(start(group), end(group))
        group = match.group()
        if group.find('.') == -1:
            return group + '.0'
        return group

    expression = expression.replace('^', '**')
    # 表达式字串提取,通过number_to_float进行浮点转换
    expression = integers_regex.sub(number_to_float, expression)
    if advanced:
        return safe_eval(expression, vars(math))
    else:
        return safe_eval(expression)


def run():
    """
    # 输入表达式,执行calc函数体
    :return:
    """
    innp = input("输入表达式: ")
    if innp is not '':
        print(calc(innp))
    else:
        print("输入为空...")
        exit()


run()
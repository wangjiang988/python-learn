#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import re


def compute_mul_div(arg):
    """ 计算乘除
    :param expression:表达式
    :return:计算结果
    """

    val = arg[0]
    mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val)
    if not mch:
        return
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val).group()

    if len(content.split('*')) > 1:
        n1, n2 = content.split('*')
        value = float(n1) * float(n2)
    else:
        n1, n2 = content.split('/')
        value = float(n1) / float(n2)

    before, after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before, value, after)
    arg[0] = new_str
    compute_mul_div(arg)


def compute_add_sub(arg):
    """ 计算加减
    :param expression:表达式
    :return:计算结果
    """
    while True:
        if arg[0].__contains__('+-') or arg[0].__contains__("++") or arg[0].__contains__('-+') or arg[0].__contains__(
                "--"):
            arg[0] = arg[0].replace('+-', '-')
            arg[0] = arg[0].replace('++', '+')
            arg[0] = arg[0].replace('-+', '-')
            arg[0] = arg[0].replace('--', '+')
        else:
            break

    if arg[0].startswith('-'):
        arg[1] += 1
        arg[0] = arg[0].replace('-', '&')
        arg[0] = arg[0].replace('+', '-')
        arg[0] = arg[0].replace('&', '+')
        arg[0] = arg[0][1:]
    val = arg[0]
    mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val)
    if not mch:
        return
    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val).group()
    if len(content.split('+')) > 1:
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)

    before, after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before, value, after)
    arg[0] = new_str
    compute_add_sub(arg)


def compute(expression):
    """ 计算加减乘除
    :param expression:表达式
    :return:计算结果
    """

    inp = [expression, 0]

    # 处理表达式中的乘除
    compute_mul_div(inp)

    # 处理
    compute_add_sub(inp)
    if divmod(inp[1], 2)[1] == 1:
        result = float(inp[0])
        result *= -1
    else:
        result = float(inp[0])
    return result


def exec_bracket(expression):
    """ 递归处理括号，并计算
    :param expression: 表达式
    :return:最终计算结果
    """
    # 如果表达式中没有括号直接调用计算函数计算并返回结果
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression):
        final = compute(expression)
        return final

    # 获取第一个只含有数字/小数和操作符的括号
    content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression).group()

    # 分割表达式
    before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression, 1)

    print('before：', expression)
    content = content[1:len(content) - 1]

    # 计算
    ret = compute(content)

    print('%s=%s' % (content, ret))

    # 拼接计算结果
    expression = "%s%s%s" % (before, ret, after)
    print('after：', expression)
    print("=" * 10, '上一次计算结束', "=" * 10)

    # 循环进行操作，直到表达式中不再含有括号为止
    return exec_bracket(expression)

# 只有执行当前文件时候,当前文件的特殊变量__name__==__main__否则不等于__main__
if __name__ == "__main__":
    print("\033[34;1m计算公式案例: 1-2*-30/-12*(-20+200*-3/-200*-300-100)\033[0m")
    string = input("请输入你要计算的公式: ")

    if string is not '':
        # string = "1-5*980.0"
        string = re.sub('\s*', '', string)
        # 表达式保存在列表中
        result = exec_bracket(string)
        print(result)
    else:
        print("\033[031;1m输入字符串为空...\033[0m")
        exit()

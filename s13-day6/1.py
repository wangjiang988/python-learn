#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-


# Author: ChenLiang

#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import math
import re

integers_regex = re.compile(r'\b[\d\.]+\b')


def calc(expression, advanced=False):
    # 将转换后的表达式通过eval来计算


    # number转换为浮点数
    def number_to_float(match):
        # 返回(start(group), end(group))
        group = match.group()
        if group.find('.') == -1:
            return group + '.0'
        return group

    expression = expression.replace('^', '**')
    expression = integers_regex.sub(number_to_float, expression)
    print(expression)

def run():
    innp = input("输入表达式: ")
    calc(innp)

run()

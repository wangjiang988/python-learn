#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lang


def strleft(str1, width, fillchar=None):
    """
    中英文混合左对齐
    :param str1: 欲对齐字符串
    :param width: 宽度
    :param fillchar: 填充字符串
    :return: 新的经过左对齐处理的字符串对象
    """
    if fillchar is None:
        fillchar = ' '
    length = len(str1.encode('gb2312'))
    fill_char_size = width - length if width >= length else 0
    return "%s%s" % (str1, fillchar * fill_char_size)


def strright(str1, width, fillchar=None):
    """
    中英文混合右对齐
    :param str1: 欲对齐字符串
    :param width: 宽度
    :param fillchar: 填充字符串
    :return: 新的经过右对齐处理的字符串对象
    """
    if fillchar is None:
        fillchar = ' '
    length = len(str1.encode('gb2312'))
    fill_char_size = width - length if width >= length else 0
    return "%s%s" % (fillchar * fill_char_size, str1)


def strcenter(str1, width, fillchar=None):
    """
    中英文混合居中对齐
    :param str1: 欲对齐字符串
    :param width: 宽度
    :param fillchar: 填充字符串
    :return: 新的经过居中对齐处理的字符串对象
    """
    if fillchar is None:
        fillchar = ' '
    length = len(str1.encode('gb2312'))
    fill_char_size = width - length if width >= length else 0
    if length % 2 == 0:
        return "%s%s%s" % (fillchar * (fill_char_size // 2), str1, fillchar * (fill_char_size // 2))
    else:
        return "%s%s%s" % (fillchar * (fill_char_size // 2 + 1), str1, fillchar * (fill_char_size // 2))


def color(str1, color_id=37):
    """
    字符串颜色高亮
    :param str1: 源字符串
    :param color_id: 颜色id：30:黑 31:红 32:绿 33:黄 34:蓝色 35:紫色 36:深绿 37:白色
    :return: 返回高亮字符串
    """
    return "\33[%sm%s\033[0m" % (color_id, str1)


def strfind(str1, sub, color_id=None):
    """
    查找子串，如果子串存在，返回的字符串中子串将被高亮
    :param str1: 字符串
    :param sub: 要查找的子串
    :param color_id: 颜色值，默认是31红色
    :return:
    """
    if color_id is None:
        color_id = 31
    return str1.replace(sub, color(sub, color_id))


def md5(str):
    """
    通过md5对字符串进行加密
    :param str: 要加密的字符串
    :return: 返回加密后的字符串
    """
    import hashlib
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()


def paging(li, max_per_page, page=1):
    """
    列表分页
    :param li: 要分页的列表
    :param max_per_page: 每页多少多个元素
    :param page: 页码
    :return: page指定页的子列表及最多可以分多少页，如果页码不存在，返回空列表
    """
    li_count = len(li)  # 列表元素的数量
    page_div = divmod(li_count, max_per_page)
    max_page = page_div[0] if page_div[1] == 0 else page_div[0] + 1  # 计算需要多少页
    if page <= max_page:
        start = ((page - 1) * max_per_page)
        end = start + max_per_page
        return li[start:end], max_page
    else:
        return [], max_page


def confirm_input(re_str, title, hint='', back_str='r', error_str='输入错误', is_pass=False):
    """
    待验证的输入（通过正则表达式进行验证）如数不合法或输入不是back_str，则提示错误并循环
    :param re_str: 正则表达式
    :param title: 输入标题
    :param hint: 输入提示
    :param back_str: 返回的字符串，遇到这个字符串将会被停止循环，并返回该字符串
    :param error_str: 输入错误时显示的字符串
    :return: 如果输入的合法返回输入的字符串，如果输入的是back_str原样返回
    """
    import re
    import getpass

    while True:
        if hint:
            print(hint)
        if is_pass:
            input_str = getpass.getpass(title).strip()
        else:
            input_str = input(title).strip()
        if input_str == back_str:
            return back_str
        if re.match(re_str, input_str):
            return input_str
        else:
            input('%s，按任意键继续' % error_str)


def logger(log_file_name, isstream=True):
    import logging
    file_handler = logging.FileHandler(log_file_name, "a", encoding="UTF-8")
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s", '%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(file_handler)
    if isstream:
        root_logger.addHandler(stream_handler)
    root_logger.setLevel(logging.INFO)
    return root_logger


def b2s(b_str, code='utf8'):
    return str(b_str, code)


def s2b(s_str, code='utf8'):
    return bytes(s_str, code)


def get_file_md5(filename):
    import os
    import hashlib
    if not os.path.isfile(filename):
        return None
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def get_space(filename):
    import os
    size = 0
    for (root, dirs, files) in os.walk(filename):
        for name in files:
            try:
                size += getsize(join(root, name))
            except:
                continue
    return size


def process_bar(start, end, width=50):
    str_num = "{:.2f}".format(start / end * 100)
    front = int(start * width / end)
    front_tag = "#" * front
    end_tag = " " * (width - front)
    tag = "{}{}".format(front_tag, end_tag)
    str_tag = "{:<7} [{}] {:,}\r".format(str_num, tag, end)
    import sys
    sys.stdout.write(str_tag)
    sys.stdout.flush()
    # time.sleep(0.1)
    if len(str_tag) == width:
        sys.stdout.write('\n')
        sys.stdout.flush()


def err(msg, quit=False):
    if quit:
        exit(color(msg, 31))
    else:
        print(color(msg, 31))

#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 多层装饰器使用(从上往下依次编译)
USER_INFO = {'is_login': True, 'user_type': 2}


def check_login(func):
    def inner(*args, **kwargs):
        if USER_INFO.get('is_login', None):
            ret = func(*args, **kwargs)
            return ret
        else:
            print("Please Login")
    return inner


def check_admin(func):
    def inner(*args, **kwargs):
        if USER_INFO.get('user_type', None) == 2:
            ret = func(*args, **kwargs)
            return ret
        else:
            print("No grants")
    return inner


@check_login
@check_admin
def index():
    """

    :return:
    """
    print('Index')


index()
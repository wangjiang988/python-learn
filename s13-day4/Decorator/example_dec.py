#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

LOGIN_INFO = {"is_login": False}


def outer(func):
    def innder():
        if LOGIN_INFO['is_login']:
            r = func()
            return r
        else:
            print("用户没有登录或者没权限查看,请先登录.")
    return innder


@outer
def order():  # 订单
    print("欢迎%s登录" % LOGIN_INFO['current_user'])


@outer
def changepwd():  # 改密码
    print("欢迎%s登录" % LOGIN_INFO['current_user'])


@outer
def manager():  # 后台管理
    print("欢迎%s登录" % LOGIN_INFO['current_user'])
    

def login(user, pwd):
    if user == 'admin' and pwd == '123':
        LOGIN_INFO['is_login'] = True
        LOGIN_INFO['current_user'] = user
        manager()


def main():
    while True:
        inp = input("1, 后台管理\n2, 登录\n")
        if inp == "1":
            manager()
        elif inp == "2":
            username = input("输入用户名: ")
            passwd = input("输入密码: ")
            login(username, passwd)

main()
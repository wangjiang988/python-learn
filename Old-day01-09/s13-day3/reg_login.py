#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


def register(username, password):
    """
    用于用户注册
    :param username: 定义新建用户名
    :param password: 定义新建密码
    :return:
    """
    with open("db", "a") as fline:
        temp = "\n" + username + "|" + password
        fline.write(temp)
        return True


def login(username, password):
    """
    用于用户登录
    :param username: 定义用户名
    :param password: 定义密码
    :return:
    """
    with open("db", "r") as fline:
        """
        # 用于用户登录
        : username:用户输入用户名
        : password:
        """
        for line in fline:
            line_list = line.strip().split("|")
            if line_list[0] == username and line_list[1] == password:
                return True
        return False


def main():
    """
    :return:
    """
    choice_num = input("1: 登录, 2: 注册: ")
    if choice_num == "1":
        user = input("Username: ")
        passwd = input("Password: ")
        lend = login(user, passwd)
        if lend:
            print("用户登录成功!!!")
        else:
            print("用户登录失败!!!")
    elif choice_num == "2":
        user = input("Username: ")
        passwd = input("Password: ")
        rend = register(user, passwd)
        if rend:
            print("用户注册成功!!!")
        else:
            print("用户这册失败!!!")

main()
#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


import re
import getpass
import sys
import os

welcome_msg = "\033[34;1m欢迎来到SHENMA用户管理系统\033[0m".center(50, '*')
select_info = "\033[34;1m1. 用户登录\n2. 用户注册\n3. 用户管理\n4. 退出\033[0m"
split_msg = ''.center(47, '*')

LOGIN_INFO = {"is_login": False}

USER_TYPE = {"is_admin": False}


def outer(func):
    """
    ; 定义装饰器用于用户登录权限控制
    :param func:
    :return:
    """
    def innder():
        if LOGIN_INFO['is_login']:
            r = func()
            return r
        else:
            print("\033[31;1m用户没有登录或者没权限查看,请先登录.\033[0m")

    return innder


def outer1(func):
    """
    ; 定义装饰器用于用户操作权限控制
    :param func:
    :return:
    """
    def innder(*args, **kwargs):
        if USER_TYPE['is_admin']:
            r = func(*args, **kwargs)
            return r
        else:
            print("\033[31;1m没有权限操作,请联系管理员.\033[0m")
    return innder


def print_info():
    """
    ; 定义打印信息函数
    :return:
    """
    try:
        print(welcome_msg)
        print(select_info)
        print(split_msg)
    except:
        return False
    else:
        return True


def register(username, password, email, phone, status="0"):
    """
    用于用户注册
    :param username: defined username info
    :param password: defined password info
    :param email: defined email info
    :param phone: defined phone number
    :param status: defined admin level
    :return:
    """
    with open("db", "a", encoding='utf-8') as obj_write:
        temp = username + "|" + password + "|" + email + "|" + phone + "|" + status + "\n"
        obj_write.write(temp)
        return True


def register_confirm():
    for i in range(3):
        input_user = input("\033[32;1mPlease enter the username: \033[0m")
        input_pass = getpass.getpass("\033[32;1mPlease enter the password: \033[0m")
        input_email = input("\033[32;1mPlease enter the email: \033[0m")
        # 正则判断用户输入是否匹配
        re_email = re.match(r"[0-9a-z]+@[0-9a-z]+\.[a-z]+", "%s" % input_email)
        input_phone = input("\033[32;1mPlease enter the phone number: \033[0m")
        re_phone = re.match(r"1+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+", "%s" % input_phone)
        print(u"\033[34;1mUser privilege\n1. Super Admin \n2. General User\033[0m")
        is_admin = input("\033[32;1mPlease enter the user type: \033[0m")
        if re_phone and re_email:
            if is_admin == "1":
                user_info = register(input_user, input_pass, input_email, input_phone, "1")
                if user_info:
                    print("\033[34;1mCreate %s Success\033[0m" % input_user)
                    break
            else:
                user_info = register(input_user, input_pass, input_email, input_phone)
                if user_info:
                    print("\033[34;1mCreate %s Success\033[0m" % input_user)
                    break
        else:
            print("\033[31;1mWarning: 您输入的邮箱或者电话有误, 请重新输入!!!\033[0m")
            continue
    else:
        print("\033[31;1mWarning: 您尝试的次数过多, 程序退出!!!\033[0m")


def login(username, password):
    """
    ; 定义登录函数用户用户登录
    :param username: 用于定义用户名
    :param password: 用于定义密码
    :return:
    """
    with open("db", "r", encoding='utf-8') as obj_read:
        for line in obj_read:
            line_list = line.strip().split("|")
            if line_list[0] == username and line_list[1] == password:
                if line_list[4] == "1":
                    USER_TYPE['is_admin'] = True
                return True
        return False


@outer
def manager():
    """
    ; 定义管理后台函数,用于控制用户查询\删除\密码更改\权限更改等操作
    :return:
    """
    # 后台管理
    print("\033[34;1m欢迎%s登录\033[0m" % LOGIN_INFO['current_user'])
    print('\033[34;1m输入你要选择的功能\033[0m'.center(52, '*'))
    print("\033[34;1m1. 用户查找\n2. 用户删除\n3. 密码修改\n4. 提升用户类型\n5. 退出\033[0m")
    manager_num = input("\033[32;1m请输入你要选择的功能继续往下操作: \033[0m")
    if manager_num == "1":
        fetch_confirm()
    elif manager_num == "2":
        remove_confirm()
    elif manager_num == "3":
        cpasswd_confirm()
    elif manager_num == "4":
        priv_confirm()
    elif manager_num == "5":
        print("欢迎下次光临")
        sys.exit()


def login_confirm():
    """
    ; 登录确认,执行登录函数
    :return:
    """
    user = input("\033[32;1mPlease enter the username: \033[0m")
    passwd = getpass.getpass("\033[32;1mPlease enter the password: \033[0m")
    lend = login(user, passwd)
    if lend:
        LOGIN_INFO['is_login'] = True
        LOGIN_INFO['current_user'] = user
        manager()
    else:
        print("\033[31;1m用户名密码错误, 或者用户名不存在, 请检查.\033[0m")


def fetch(user):
    """
    ; 定义fetch函数,用于搜索用户信息
    :param user:
    :return:
    """
    print("\033[32;1m用户查询的相关用户或者邮箱信息如下:\033[0m")
    with open("db", "r", encoding='utf-8') as obj_read:
        for line in obj_read:
            line_list = line.strip().split("|")
            if USER_TYPE['is_admin'] and user == line_list[0] or user in line_list[2]:
                name = line_list[0]
                mail = line_list[2]
                phone = line_list[3]
                utype = line_list[4]
                if utype == "1":
                    priv = "Admin"
                else:
                    priv = "User"
                print(u"\033[34;1m用户名: {0:s}  Password: ****** Email: {1:s}  Phone: {2:s}  账号类型: {3:s}\033[0m".format(name, mail, phone, priv))


@outer
@outer1
def fetch_confirm():
    """
    ; 执行用户查找操作
    :return:
    """
    fetch_info = input("\033[32;1m请输入你要查询的用户信息,可按照邮箱和用户名来搜索: \033[0m")
    re_user = re.match(r"[0-9a-z]+", "%s" % fetch_info)
    re_email = re.match(r"[0-9a-z]+@[0-9a-z]+\.[a-z]+", "%s" % fetch_info)
    if re_user or re_email and LOGIN_INFO['is_login'] == True:
        fetch(fetch_info)


def remove(user):
    """
    ; 定义移除用户操作函数
    :param user:
    :return:
    """
    with open("db", "r", encoding='utf-8') as obj_read, open("db1", "a", encoding='utf-8') as obj_write:
        flag = False
        for line in obj_read:
            if flag is not True and user in line.strip():
                continue
            else:
                obj_write.write(line)

        os.rename('db1', 'db')


@outer
@outer1
def remove_confirm():
    """
    ; 执行用户删除确认
    :return:
    """
    remove_user = input("\033[32;1m请输入你要删除的用户: \033[0m")
    re_user = re.match(r"[a-z]+", "%s" % remove_user)
    if re_user and LOGIN_INFO['is_login'] == True:
        remove(remove_user)
        print("\033[34;1m用户 %s 删除成功\033[0m" % remove_user)
    else:
        print("\033[31;1m输入用户名不存在\033[0m")


def changepwd(user, passwd):
    """
    ; 定义用户密码更改函数
    :param user:
    :param passwd:
    :return:
    """
    with open("db", "r", encoding='utf-8') as obj_read, open("db1", "w", encoding='utf-8') as obj_write:
        for line in obj_read:
            line_list = line.strip().split("|")
            if USER_TYPE['is_admin'] and user == line_list[0]:
                name = line_list[0]
                password = passwd
                mail = line_list[2]
                phone = line_list[3]
                utype = line_list[4]
                temp = name + "|" + password + "|" + mail + "|" + phone + "|" + utype + "\n"
                obj_write.write(temp)
                continue
            obj_write.write(line)

        os.rename("db1", "db")


@outer
@outer1
def cpasswd_confirm():
    """
    ; 用于确认用户密码更改操作
    :return:
    """
    change_user = input("\033[32;1m请输入你要修改密码的用户: \033[0m")
    change_passwd = getpass.getpass("\033[32;1mPlease enter the password: \033[0m")
    confirm_passwd = getpass.getpass("\033[32;1mPlease again confirm password: \033[0m")
    if change_user and LOGIN_INFO['is_login'] == True and change_passwd == confirm_passwd:
        changepwd(change_user, change_passwd)
        print("\033[34;1m用户 %s 密码修改成功\033[0m" % change_user)
    else:
        print("\033[31;1m用户密码更改失败\033[0m")


def change_priv(user):
    """
    ; 定义用户权限更改函数
    :param user:
    :return:
    """
    with open("db", "r", encoding='utf-8') as obj_read, open("db1", "w", encoding='utf-8') as obj_write:
        for line in obj_read:
            line_list = line.strip().split("|")
            if USER_TYPE['is_admin'] and user == line_list[0]:
                name = line_list[0]
                passwd = line_list[1]
                mail = line_list[2]
                phone = line_list[3]
                utype = "1"
                temp = name + "|" + passwd + "|" + mail + "|" + phone + "|" + utype + "\n"
                obj_write.write(temp)
                continue
            obj_write.write(line)

        os.rename("db1", "db")


@outer
@outer1
def priv_confirm():
    """
    ; 确认用户权限更改操作
    :return:
    """
    priv_user = input("\033[32;1m请输入你要提权的用户: \033[0m")
    if priv_user and LOGIN_INFO['is_login'] == True:
        change_priv(priv_user)
        print("\033[34;1m用户 %s 提权成功\033[0m" % priv_user)
    else:
        print("\033[31;1m用户提权操作失败\033[0m")


def main():
    """
    ; 定义主函数
    :return:
    """
    while True:
        print_info()
        print("\033[32;1m请按照以上编号选择对应功能继续往下执行 \033[0m")
        num_input = int(input("\033[32;1mPlease enter the number: \033[0m"))
        if num_input == 1:
            login_confirm()
            break
        elif num_input == 2:
            register_confirm()
            break
        elif num_input == 3:
            manager()
        elif num_input == 4:
            print("\033[31;1m欢迎下次光临\033[0m")
            sys.exit()


main()
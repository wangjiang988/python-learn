#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import getpass  # 导入getpass模块
import time  # 导入时间模块

init_count = 0  # 定义密码次数初始计数器

valid_users = {
    'chenliang': "chenliang",
    'chenlong': "chenlong"
}  # 定义一个字典,用于存储用户名及密码信息

for i in range(3):  # 利用for循环进行计数
    username = input("请输入您的用户名: ")  # 定义用户名变量,用来存储用户输入的用户信息
    if len(username) == 0:  # 判断username变量长度是否为0
        print("您好,用户名不能为空,请重新输入...")
        continue  # 跳出当前,继续执行下面的代码
    else:
        file = open("user.txt", "r")  # 调用open方法,以只读方式读取user.txt的文件
        index = 0  # 定义user.txt文件行初始计数器
        valid = True  # 定义变量为真,供后面调用
        rm_file_line = False  # 定义变量为假,供后面调用
        lines = file.readlines()  # 读行
        file.close()  # 调用close方法关闭文件
        for line in lines:  # for循环取行信息
            name = line.split(" ")[0]  # 根据行取出第一列内容
            t = line.split(" ")[1]  # 根据行取出第二列内容
            if name == username and time.time() - float(t) <= 60:  # 判断用户名是否相同,同时时间是否小于等于60s
                valid = False  # 为假,进行账户锁定操作,同时退出程序
                print("账户锁定,请一分钟后尝试登录...")
                break
            elif name == username and time.time() - float(t) > 60:  # 判断用户名是否相同,同时时间是否大于60s
                rm_file_line = True  # 为真,进行账户记录行移除操作
                break
            index += 1  # 计数器自加

        if valid:  # 判断valid的值,如果为True,进行下一步判断,如果为False继续锁定账号
            if rm_file_line:  # 判断rm_file_line的值, 如果为True,清除锁定账号,如果为False,继续以一步判断
                lines.remove(lines[index])  # 调用remove方法删除行
                file = open("user.txt", "w+")  # 调用open方法
                file.writelines(lines)  # 调用writelines方法
                file.close()  # 调用close方法
            if username in valid_users.keys():  # 判断username的值在valid_users字典中是否存在
                while init_count < 3:  # while判断
                    password = getpass.getpass("请输入用户密码信息: ")  # 定义密码变量,用来存储用户输入的密码信息
                    if len(password) == 0 or password != valid_users[username]:  # 判断用户密码长度已经用户与密码是否匹配
                        print("用户名和密码不匹配,请重新输入...")
                        init_count += 1  # 自加,用于记录计数器的值
                        continue  # 跳出当前
                    else:  # 如果用户名和密码对应,打印欢迎界面
                        print("欢迎登录管理系统, %s" % username)
                        break
                if 3 == init_count:  # 判断如果计数器为3,锁定用户登录
                    print("账号输入次数过多,账号已经锁定!")
                    file = open("user.txt", "a")  # 调用open方法
                    file.write("%s %s\n" % (username, time.time()))  # 记录锁定的用户信息到文件
                    file.close()  # 调用close方法关闭文件
            else:  # 如果输入的用户名不存在,退出并打印信息
                print("您输入的用户名不存在,Bye!")
    break

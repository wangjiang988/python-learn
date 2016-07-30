#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 形式参数传参
"""
1、普通参数
2、默认参数(给某个参数指定默认参数，那么这个形式参数必须放在结尾，不能这样写(xx, yy="yes", oo))
3、指定参数(可以自定义参数位置调用)
"""


def sendmail(r_user, content, r_text):  # 指定普通参数
    try:  # 捕捉异常
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["SmartCZM", '18701115239@163.com'])
        msg['To'] = formataddr([r_text, '554248852@@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("18701115239@163.com", "06020655czm")
        server.sendmail('18701115239@163.com', [r_user, ], msg.as_string())
        server.quit()
    except:  # 发送失败执行
        return False
    else:  # 发送成功执行
        return True
    # 在函数中,一旦遇到return,函数执行过程立即终止

# 循环传参数发送
while True:
    mail_address = input("Email Input: ")
    ret = sendmail(mail_address, "Welcome", "Guys")
    if ret:
        print("发送成功")
    else:
        print("发送失败")


def sendmail(r_user, content, r_text):  # 默认参数
    try:  # 捕捉异常
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["SmartCZM", '18701115239@163.com'])
        msg['To'] = formataddr([r_text, '554248852@@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("18701115239@163.com", "06020655czm")
        server.sendmail('18701115239@163.com', [r_user, ], msg.as_string())
        server.quit()
    except:  # 发送失败执行
        return False
    else:  # 发送成功执行
        return True
    # 在函数中,一旦遇到return,函数执行过程立即终止

# 循环传参数发送
while True:
    mail_address = input("Email Input: ")
    ret = sendmail(mail_address, "Welcome", "Guys")
    if ret:
        print("发送成功")
    else:
        print("发送失败")


def sendmail(r_user, content, r_text):  # 指定参数
    try:  # 捕捉异常
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["SmartCZM", '18701115239@163.com'])
        msg['To'] = formataddr([r_text, '554248852@@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("18701115239@163.com", "06020655czm")
        server.sendmail('18701115239@163.com', [r_user, ], msg.as_string())
        server.quit()
    except:  # 发送失败执行
        return False
    else:  # 发送成功执行
        return True
    # 在函数中,一旦遇到return,函数执行过程立即终止

# 循环传参数发送
while True:
    mail_address = input("Email Input: ")
    ret = sendmail(mail_address, "Welcome", "Guys")
    if ret:
        print("发送成功")
    else:
        print("发送失败")


def text(*args):  # 指多个参数,动态传参
    print(args)


text('k1', 'k2', 'k3', 'k4')

加* 和 不加* 接收参数的区别
ret = sendmail(args)  # 如果元素是列表,会将整个列表当成一个独立参数存在在元组中.
ret = sendmail(*args)  # 如果元素是列表,会将列表中的每个元素独立存放在元组中.

函数补充
* Python默认执行会依次往下执行
def f1(a1, a2):
    return a1 + a2


def f1(a1, a2):
    return a1 * a2


ret = f1(8, 8)
print(ret)


* 对于函数来说,Python传递参数的时候传递的是一份引用,而不是copy
def f1(a1):
    a1.append(9999)


li = [11, 22, 33, 44]
f1(li)

print(li)


* 全局变量, 对于函数体来说，自己本身创建的变量，只能用于自己本身的作用域，而不能被全局调用
def f1():
    name = 'admin'
    print(name)


def f2():
    print(name)

f1()
f2()

NAME = 'admin'  # 函数体之外创建，全局变量


def f1():
    age = 18
    # global NAME  # 表示，name是全局变量,修改全局变量用
    name = 'chenliang'
    print(age, name)


def f2():
    age = 19
    print(age, NAME)


f1()
f2()

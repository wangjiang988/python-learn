#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


def sendmail(r_user, content):  # 形式参数,传递变量参数,可以传递多个形式参数
    try:  # 捕捉异常
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["ChenLiang", '18701115239@163.com'])
        msg['To'] = formataddr(["走人", '554248852@@qq.com'])
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

# 具体传值,实际参数
# ret = sendmail("554248852@qq.com")
# if ret:
#     print("发送成功")
# else:
#     print("发送失败")

# 循环传参数发送
while True:
    mail_address = input("Email Input: ")
    ret = sendmail(mail_address, "Welcome")
    if ret:
        print("发送成功")
    else:
        print("发送失败")
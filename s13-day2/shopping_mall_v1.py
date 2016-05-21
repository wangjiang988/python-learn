#!/usr/bin/env python3.5
# Author: ChenLiang

import time
import getpass
from datetime import datetime
import sys
import codecs

prod_list = {
    '汽车类': {'Benz': 1000000, 'BMW': 2000000, 'Audi': 800000, 'Tesla': 820000},
    '家电类': {'电视机': 3400, '电冰箱': 6000, '洗衣机': 8000, '电饭煲': '500'},
    '手机类': {'Apple': 5600, 'Mi2': 2000, 'HuaWeiMeta8': 5600},
}

shop_car = {}  # 定义购物车变量
salary = 100000
money_total = 0
s_time = ''


def print_shop_car():  # 定义函数,供程序调用
    print("购物车".center(50, "*"))
    data = shop_car
    if s_time != '':
        print("订单生成时间为: ", s_time)
        print("id".ljust(20, " "), "p_name".ljust(20, " "), "num".center(16, " "), "total_price".rjust(22, " "))
        for data_id, data_key in enumerate(data):
            print(int(data_id + 1), ".", "".ljust(18, " "), data_key, "".rjust(20, " "), int(data[data_key][0]),
                  "".rjust(24, " "), int(data[data_key][2]))
        print("END".center(58, "*"))
        print("您的余额为: \033[32;1m%s\033[0m" % salary)
    else:
        print("\033[31;1m没有生成订单记录,请开始购物\033[0m")
    return


def sel_history():  # 定义函数,供程序调用
    with codecs.open("dump.txt", "r", "utf-8") as o_his:
        o_line = o_his.readlines()
        for i_line in o_line:
            print(i_line)


def user_info():  # 定义函数,供程序调用
    shop_user = username
    print(u"欢迎登录商场购物平台, {0:s}".format(shop_user))


welcome_msg = '欢迎来到新世纪购物中心'.center(50, '-')  # 定义环境信息
print(welcome_msg)
welcome_info = """\033[33;1m
请先创建用户或者登录平台进行购物:
1: 用户注册
2: 用户登录
3: 退出系统
\033[0m""".center(159, '*')

shop_select = """\033[33;1m
请选择编号继续进行购物:
a: 开始购物
c: 查看购物车
m: 充值
b: 返回主界面
h: 查看历史购买信息
q: 退出系统
\033[0m""".center(159, '*')
while True:
    print(welcome_info)
    u_choice = input("请输入你要选择的编号: ")
    if u_choice.isdigit():
        u_choice = int(u_choice)
        if u_choice == 1:
            while True:
                with open("name.txt", 'r')as read_1:  # 打开name.txt文件并保证正常关闭
                    temp = read_1.readlines()
                    t_list = []
                for t_line in temp:
                    t_line = t_line.strip().split(":")
                    t_list.append(t_line[0])
                add_user = input("请输入你要创建的用户名: ")
                ses = "成功创建用户%s" % add_user
                if add_user in t_list:
                    print("输入的用户名已存在,请重新输入".center(50, '-'))
                elif add_user == '':
                    print("输入的用户名为空,Bye".center(50, '-'))
                    break
                else:
                    add_pass = getpass.getpass("请创建一个新的用户密码,复杂度请满足数字加字母,长度为8位: ")
                    conf_pass = getpass.getpass("请再次确认创建的用户密码: ")
                    if add_pass != conf_pass:
                        print("两次输入的用户密码不匹配,请重新确认输入...")
                    elif len(add_pass) == '':
                        print("输入的密码为空,请重新输入...")
                    elif len(add_pass) < 8 or add_pass.isalnum() == False:
                        print("输入的密码复杂度不够或者长度不为8位,请重新输入...")
                    else:
                        with open("name.txt", 'a') as read_2:
                            write_line = "%s:%s:0\n" % (add_user, add_pass)
                            read_2.write(write_line)
                            print(ses.center(50, '-'))
                            break
        if u_choice == 2:
            exit_flag = False
            while True:
                init_count = 0
                username = input("请输入您的用户名: ")  # 定义用户名变量,用来存储用户输入的用户信息
                if len(username) == 0:  # 判断username变量长度是否为0
                    print("\033[31;1m您好,用户名不能为空,请重新输入!!!\033[0m")
                    continue  # 跳出当前,继续执行下面的代码
                else:
                    with open("lock.txt", "r") as read_3:
                        index = 0  # 定义user.txt文件行初始计数器
                        valid = True  # 定义变量为真,供后面调用
                        rm_file_line = False  # 定义变量为假,供后面调用
                        lines = read_3.readlines()  # 读行
                    for line in lines:  # for循环取行信息
                        name = line.split(" ")[0]  # 根据行取出第一列内容
                        t = line.split(" ")[1]  # 根据行取出第二列内容
                        if name == username and time.time() - float(t) <= 60:  # 判断用户名是否相同,同时时间是否小于等于60s
                            valid = False  # 为假,进行账户锁定操作,同时退出程序
                            print("\033[31;1m账户锁定,请一分钟后尝试登录!!!\033[0m")
                            break
                        elif name == username and time.time() - float(t) > 60:  # 判断用户名是否相同,同时时间是否大于60s
                            rm_file_line = True  # 为真,进行账户记录行移除操作
                            break
                        index += 1  # 计数器自加

                    if valid:  # 判断valid的值,如果为True,进行下一步判断,如果为False继续锁定账号
                        if rm_file_line:  # 判断rm_file_line的值, 如果为True,清除锁定账号,如果为False,继续以一步判断
                            lines.remove(lines[index])  # 调用remove方法删除行
                            with open("lock.txt", "w+") as read_4:
                                read_4.writelines(lines)  # 调用writelines方法
                        with open("name.txt", "r") as read_5:
                            for user_line in read_5.readlines():
                                user, passwd, money = user_line.strip().split(":")
                                if username == user:  # 判断username的值在valid_users字典中是否存在
                                    while init_count < 3:  # while判断
                                        password = getpass.getpass("请输入用户密码信息: ")  # 定义密码变量,用来存储用户输入的密码信息
                                        if len(password) == 0 or password != passwd:  # 判断用户密码长度已经用户与密码是否匹配
                                            print("\033[31;1m用户名和密码不匹配,请重新输入!!!\033[0m")
                                            init_count += 1  # 自加,用于记录计数器的值
                                            continue  # 跳出当前
                                        else:  # 如果用户名和密码对应,打印欢迎界面
                                            print(u"欢迎登录商场购物平台, {0:s}".format(username))
                                            with codecs.open("dump.txt", "a", "utf-8") as user_shop:
                                                user_shop.write("用户" + str(username) + "购物历史:" + '\n')
                                            break
                                    if 3 == init_count:  # 判断如果计数器为3,锁定用户登录
                                        print("\033[31;1m账号输入次数过多,账号已经锁定!!!\033[0m")
                                        with open("lock.txt", "a") as read_6:
                                            read_6.write("%s %s\n" % (username, time.time()))
                                else:  # 如果输入的用户名不存在,退出并打印信息
                                    print("您输入的用户名不存在,请先注册用户")
                                    sys.exit()
                break
            exit_flag = False
            while True:
                print(shop_select)
                num_choice = input("您输入您的选择: ")  # 定义用户输入变量
                if num_choice == 'm':
                    credit = input("请输入你要充值的金额: ")
                    com_pass = input("请输入密码确认充值: ")
                    if credit.isdigit():
                        credit = int(credit)
                        with open("name.txt", "r+") as read_8:
                            for user_line in read_8.readlines():
                                user, passwd, money = user_line.strip().split(":")
                                if com_pass == passwd:
                                    money_add = (credit + int(money))
                                    write_money = "%s:%s:%s\n" % (user, passwd, money_add)
                                    read_8.seek(0, 0)  # 还原文件偏移位置
                                    read_8.write(write_money)
                                    print("充值成功,充值金额为: \033[31;1m%s\033[0m,当前余额为: \033[31m;1m%s\033[0m" % (
                                        credit, money_add))
                                    salary = (salary + money_add)
                                    exit_flag = True
                                    break
                                continue
                            break
                elif num_choice == 'a':
                    print("\033[31;0m商品列表\033[0m".center(55, "-"))  # 格式化输出
                    for v, item in enumerate(prod_list.keys()):
                        print(v, ":", item)
                    user_choice = input("您输入您需要购买的商品分类编号?: ")  # 定义用户输入变量
                    if user_choice.isdigit():  # 肯定是选择商品,判断是否输入为数字
                        user_choice = int(user_choice)  # 将用户的输入转换为整形
                        if user_choice < len(prod_list):  # 判断用户选择是否超出商品列表长度
                            for key_m, item_value in enumerate(prod_list.keys()):
                                if user_choice == key_m:
                                    for key_1, value_1 in enumerate(prod_list[item_value]):
                                        print(key_1, value_1)
                                    user_c = input("输入你要选择的商品编号: ")
                                    if user_c.isdigit():
                                        user_c = int(user_c)
                                        if user_c < len(prod_list[item_value]):
                                            for key_2, value_2 in enumerate(prod_list[item_value]):
                                                if user_c == key_2:
                                                    p_money = prod_list[item_value].get(value_2)
                                                    p_money = int(p_money)
                                                    user_shop_num = input("请输入您需要购买的商品数量: ")
                                                    if user_shop_num.isdigit():
                                                        user_shop_num = int(user_shop_num)
                                                        car_int = 0
                                                        for snum in range(user_shop_num):
                                                            if p_money <= salary:  # 判断商品金额是否小于或者等于工资金额,小于则可以购买,否则提示余额不足
                                                                buy_pool = [value_2]
                                                                num = 1
                                                                spend = p_money
                                                                s_time = datetime.now()
                                                                if buy_pool[0] not in shop_car.keys():
                                                                    # 如果不在则直接加入购物车
                                                                    shop_car[buy_pool[0]] = [num, value_2, spend]
                                                                else:
                                                                    # 修改购物车中商品的个数及总金额
                                                                    shop_car[buy_pool[0]][0] = int(
                                                                        shop_car[buy_pool[0]][0]) + int(num)
                                                                    shop_car[buy_pool[0]][2] = int(
                                                                        shop_car[buy_pool[0]][2]) + int(spend)
                                                                salary -= p_money  # 扣钱
                                                                with open("name.txt", "r+") as read_9:
                                                                    for user_9 in read_9.readlines():
                                                                        _user, _passwd, _money = user_9.strip().split(
                                                                            ":")
                                                                        m_money = "%s:%s:%s\n" % (
                                                                            _user, _passwd, salary)
                                                                        read_9.seek(0, 0)  # 还原文件偏移位置
                                                                        read_9.write(m_money)
                                                                car_int += 1
                                                                money_total += p_money
                                                                print(
                                                                    "已添加商品 %s x %s 到购物车, 购买时间为: %s, 总价为: %s, 您当前余额为, \033[31;1m%s\033[0m" % (
                                                                        value_2, car_int, s_time,
                                                                        money_total,
                                                                        salary))  # 打印购买商品信息,同时显示余额信息
                                                                his_list = (
                                                                    "已添加商品 %s x %s 到购物车, 购买时间为: %s, 总价为: %s, 您当前余额为, %s" % (
                                                                        value_2, car_int, s_time,
                                                                        money_total,
                                                                        salary))
                                                                with codecs.open("dump.txt", "a", "utf-8") as his_shop:
                                                                    his_shop.seek(0, 0)
                                                                    his_shop.write(str(his_list) + '\n')
                                                            else:
                                                                print(
                                                                    "您的余额不足以购买此产品: \033[32;1m%s\033[0m,请进行充值" % salary)  # 余额不足提示
                                                    else:
                                                        print("\033[31;1m输入错误,请重新输入!!!\033[0m")
                                                        continue
                                    else:
                                        print("\033[31;1m输入错误,请重新输入!!!\033[0m")
                                        continue
                    else:
                        print("\033[31;1m输入错误,返回上一级菜单!!!\033[0m")
                        exit_flag = True
                        break
                elif num_choice == 'h' or num_choice == 'history':
                    sel_history()
                    continue
                elif num_choice == 'b' or num_choice == 'back':
                    exit_flag = True
                    break
                else:
                    if num_choice == 'q' or num_choice == 'quit':  # 判断用户选择q或者quit,就退出系统,同时打印用户购买商品列表
                        print_shop_car()
                        print("\033[33;1m欢迎下次光临新世纪购物中心,Bye!\033[0m")
                        break
                    elif num_choice == 'c' or num_choice == 'check':  # 判断用户选择c或者check,打印用户购买商品列表,同时提示余额信息
                        print_shop_car()
        if u_choice == 3:
            print("\033[33;1m欢迎下次光临新世纪购物中心,Bye!\033[0m")
            break
    print("\033[31;1mWarning: 不能找到对应的编号,请重新输入!!!\033[0m")
    continue

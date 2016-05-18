#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

salary = input("请输入您的工资金额: ")  # 定义salary变量,用于后续判断
if salary.isdigit():  # 判断输入内容是否为数字
    salary = int(salary)  # 转换为整形
else:
    exit("无效的数据类型,谢谢.")

welcome_msg = '欢迎来到新世纪购物中心'.center(50, '-')  # 定义环境信息

print(welcome_msg)

exit_flag = False  # 定义退出标志位,用于结束循环使用
product_list = [  # 定义商品列表
    ('Iphone', 5888),
    ('Mac Air', 8000),
    ('Mac Pro', 9000),
    ('Mi 2', 1999),
    ('Coffee', 30),
    ('Tesla', 820000),
    ('bike', 700),
    ('Cloth', 200),
]

shop_car = []  # 定义购物车变量

while not exit_flag:  # 当exit_flag标志位不为True,执行后面的代码
    # while exit_flag is not True:
    # for product_item in product_list:
    #    p_name,p_price = product_item
    # enumerate 枚举函数,打印下标
    print("商品列表".center(55, "-"))  # 格式化输出
    for item in enumerate(product_list):  # 循环枚举商品列表,打印商品编号及商品信息
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(index, ':', p_name, p_price)

    user_choice = input("[q=quit,c=check]您输入您需要购买的产品编号?: ")  # 定义用户输入变量
    if user_choice.isdigit():  # 肯定是选择商品,判断是否输入为数字
        user_choice = int(user_choice)  # 将用户的输入转换为整形
        if user_choice < len(product_list):  # 判断用户选择是否超出商品列表长度
            p_item = product_list[user_choice]  # 获取用户选择的商品
            if p_item[1] <= salary:  # 判断商品金额是否小于或者等于工资金额,小于则可以购买,否则提示余额不足
                shop_car.append(p_item)  # 放入购物车
                salary -= p_item[1]  # 扣钱
                print("已添加商品 %s 到购物车, 您当前余额为, \033[31;1m%s\033[0m" % (list(p_item), salary))  # 打印购买商品信息,同时显示余额信息
            else:
                print("您的余额不足以购买此产品: \033[32;1m%s\033[0m" % salary)  # 余额不足提示
    else:
        if user_choice == 'q' or user_choice == 'quit':  # 判断用户选择q或者quit,就退出系统,同时打印用户购买商品列表
            print("您所购买的产品信息如下".center(50, "*"))
            for item in shop_car:
                print(list(item))
            print("购物结束".center(55, "*"))
            print("您的余额为: \033[32;1m%s\033[0m" % salary)
            print("Bye")
            exit_flag = True
        elif user_choice == 'c' or user_choice == 'check':  # 判断用户选择c或者check,打印用户购买商品列表,同时提示余额信息
            print("您所购买的产品信息如下".center(50, "*"))
            for item in shop_car:
                print(list(item))
            print("END".center(58, "*"))
            print("您的余额为: \033[32;1m%s\033[0m" % salary)

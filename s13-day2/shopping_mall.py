#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

salary = input("请输入您的工资金额: ")
if salary.isdigit():
    salary = int(salary)
else:
    exit("无效的数据类型,谢谢.")

welcome_msg = '欢迎来到新世纪购物中心'.center(50, '-')

print(welcome_msg)

exit_flag = False
product_list = [
    ('Iphone', 5888),
    ('Mac Air', 8000),
    ('Mac Pro', 9000),
    ('Mi 2', 1999),
    ('Coffee', 30),
    ('Tesla', 820000),
    ('bike', 700),
    ('Cloth', 200),
]

shop_car = []

while not exit_flag:
    # while exit_flag is not True:
    # for product_item in product_list:
    #    p_name,p_price = product_item
    # enumerate 枚举函数,打印下标
    print("商品列表".center(55, "-"))
    for item in enumerate(product_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(index, ':', p_name, p_price)

    user_choice = input("[q=quit,c=check]您输入您需要购买的产品编号?: ")
    if user_choice.isdigit():  # 肯定是选择商品
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary:  # 可以购买
                shop_car.append(p_item)  # 放入购物车
                salary -= p_item[1]  # 扣钱
                print("已添加商品 %s 到购物车, 您当前余额为, \033[31;1m%s\033[0m" %
                      (list(p_item), salary))
            else:
                print("您的余额不足以购买此产品: \033[32;1m%s\033[0m 当前余额: \033[32;1m%s\033[0m" % p_item, salary)
    else:
        if user_choice == 'q' or user_choice == 'quit':
            print("您所购买的产品信息如下".center(50, "*"))
            for item in shop_car:
                print(list(item))
            print("购物结束".center(55, "*"))
            print("您的余额为: \033[32;1m%s\033[0m" % salary)
            print("Bye")
            exit_flag = True
        elif user_choice == 'c' or user_choice == 'check':
            print("您所购买的产品信息如下".center(50, "*"))
            for item in shop_car:
                print(list(item))
            print("END".center(58, "*"))
            print("您的余额为: \033[32;1m%s\033[0m" % salary)

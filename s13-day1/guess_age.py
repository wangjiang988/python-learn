#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 多重if判断猜数字大小
# age = 25
#
# guess_number = int(input("Input your guess num: "))
# if guess_number == age:
#     print("Congratulations! you got it.")
# elif guess_number > age:
#     print("Think Smaller!")
# else:
#     print("Think Big...")

# for循环配合if猜数字大小
# age = 25
#
# for i in range(10):
#     guess_number = int(input("Input your guess num: "))
#     if i < 3:
#         if guess_number == age:
#             print("Congratulations! you got it.")
#             break  # 不往下执行,跳出整个循环体
#         elif guess_number > age:
#             print("Think Smaller!")
#         else:
#             print("Think Big...")
#     else:
#         print("too many attempts...bye")
#         break
#
# # 根据用户输入来判断是否继续(此方案不成立)
# age = 25
#
# for i in range(10):
#     if i < 3:
#         guess_number = int(input("Input your guess num: "))
#         if guess_number == age:
#             print("Congratulations! you got it.")
#             break  # 不往下执行,跳出整个循环体
#         elif guess_number > age:
#             print("Think Smaller!")
#         else:
#             print("Think Big...")
#     else:
# #        print("too many attempts...bye")
# #        break
#         continue_confirm = input("Do you want to continue yes or no?")
#         if continue_confirm == 'yes':
#             i = 0
#             # pass # 不做任何操作
#         else:
#             print("bye")
#             break

# 根据用户输入来判断是否继续,加入标志为来配合判断.
age = 25
counter = 0
for i in range(10):
    print("--counter:", counter)
    if counter < 3:
        guess_number = int(input("Input your guess num: "))
        if guess_number == age:
            print("Congratulations! you got it.")
            break  # 不往下执行,跳出整个循环体
        elif guess_number > age:
            print("Think Smaller!")
        else:
            print("Think Big...")
    else:
        continue_confirm = input("Do you want to continue yes or no?")
        if continue_confirm == 'yes':
            counter = 0
            # pass # 不做任何操作
            continue
        else:
            print("Ok,bye")
            break
    counter += 1



多级菜单:
1. 北京
2. 上海
3. 四川

>>> :1
    1. 东城
    2. 西城
    3. 朝阳
>>> :2

b 返回上一层
q 退出

作业需求流程图

作业目录：day1
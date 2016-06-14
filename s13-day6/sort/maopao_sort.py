#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


def bubblesort(numbers):
    for num in range(len(numbers) - 1, 0, -1):
        for i in range(num):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                # print(i, num)
                # print(numbers)
    return numbers


# 第一步
li = [13, 22, 6, 99, 11]

for m in range(4):  # 等价于 #for m in range(len(li)-1):
    if li[m] > li[m + 1]:
        temp = li[m + 1]
        li[m + 1] = li[m]
        li[m] = temp
print(li)

# 第二步
li = [13, 22, 6, 99, 11]

for m in range(4):  # 等价于 #for m in range(len(li)-1):
    if li[m] > li[m + 1]:
        temp = li[m + 1]
        li[m + 1] = li[m]
        li[m] = temp

for m in range(3):  # 等价于 #for m in range(len(li)-2):
    if li[m] > li[m + 1]:
        temp = li[m + 1]
        li[m + 1] = li[m]
        li[m] = temp

for m in range(2):  # 等价于 #for m in range(len(li)-3):
    if li[m] > li[m + 1]:
        temp = li[m + 1]
        li[m + 1] = li[m]
        li[m] = temp

for m in range(1):  # 等价于 #for m in range(len(li)-4)
    if li[m] > li[m + 1]:
        temp = li[m + 1]
        li[m + 1] = li[m]
        li[m] = temp
print(li)

# 第三步
li = [13, 22, 6, 99, 11]

for i in range(1, 5):
    for m in range(len(li) - i):
        if li[m] > li[m + 1]:
            temp = li[m + 1]
            li[m + 1] = li[m]
            li[m] = temp
print(li)
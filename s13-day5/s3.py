#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# Python 叫模块,其他叫 类库
"""
模块，用一砣代码实现了某个功能的代码集合。

类似于函数式编程和面向过程编程，函数式编程则完成一个功能，其他代码用来调用即可，提供了代码的重用性和代码间的耦合。而对于一个复杂的功能来，可能需要多个函数才能完成（函数又可以在不同的.py文件中），n个 .py 文件组成的代码集合就称为模块。

如：os 是系统相关的模块；file是文件操作相关的模块

模块分为三种：

自定义模块
第三方模块
内置模块

"""
"""
# 自定义模块
文件
1. 新建src.py文件
2. 在index.py主文件中import src 导入src模块
现在即可调用src中的函数
文件夹
1. 新建lib文件夹,同时在下面创建comm.py文件
2. 在index.py主文件中import lib.comm 导入lib文件夹下面的comm文件
现在即可调用comm中的函数

Python之所以应用越来越广泛，在一定程度上也依赖于其为程序员提供了大量的模块以供使用，如果想要使用模块，则需要导入。导入模块有一下几种方法：

import module  # 单模块, 同一级目录下推荐导入方式
from module.xx.xx import xx  # 嵌套文件夹, 推荐导入方式
from module.xx.xx import xx as rename # 对于多文件夹重复的模块导入, 推荐导入方式
from module.xx.xx import *  # 导入module.xx.xx下面所有的模块, 不推荐这样用

导入模块其实就是告诉Python解释器去解释那个py文件

导入一个py文件，解释器解释该py文件
导入一个包，解释器解释该包下的 __init__.py 文件 【py2.7】
那么问题来了，导入模块时是根据那个路径作为基准来进行的呢？即：sys.path

import sys
for key in sys.path:
    print(key)

如果sys.path路径列表没有你想要的路径，可以通过 sys.path.append('路径') 添加。
sys.path.append('E:\\')

模块名称的重要性: 不能和系统内置模块重名
"""

# import sys
#
# print(sys.argv)  # 执行脚本传参
# for key in sys.path:
#     print(key)

# 内置模块
# 内置模块是Python自带的功能，在使用内置模块相应的功能时，需要【先导入】再【使用】
"""
1. 序列化和反序列化
Python中用于序列化的两个模块

json     用于【字符串】和 【python基本数据类型】 间进行转换,更加适合跨语言
pickle   用于【python特有的类型】 和 【python基本数据类型】间进行转换,更加适合python所有类型的序列化,只适用于python
Json模块提供了四个功能：dumps、dump、loads、load

pickle模块提供了四个功能：dumps、dump、loads、load  # 通过特殊方式处理只能python语言识别的字符串
游戏存档就是利用pickle来操作的


import json

dic = {'k1': 'v1'}
print(dic, type(dic))

# 将python基本数据类型转化成字符串形式
result = json.dumps(dic)
print(result, type(result))


string = '{"Year": 2016}'  # 通过loads去做反序列化的时候,一定要记住使用双引号
print(string, type(string))

# 将字符串形式转化成基本数据类型
str_inp = json.loads(string)
print(str_inp, type(str_inp))

例子:
# 获取天气信息
import requests
import json

response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
response.encoding = 'utf-8'

dic = json.loads(response.text)  # .text返回的内容
for key in dic:
    print(key, dic[key])


import json

# dump , load 读文件写文件操作

li = [11, 22, 33]
# 将数据通过特殊的形式转换只有python语言认识的字符串,并写入文件
json.dump(li, open('db', 'w'))
print(type(li), li)

# 将输入通过特殊的形式转换为所有程序语言都认识的字符串,并读出文件
li = json.load(open('db', 'r'))
print(type(li), li)

# pickle
import pickle

li = [11, 22, 33]
result = pickle.dumps(li)

print(result, type(result))

li = [11, 22, 33]
result = pickle.loads(result)
print(result, type(result))

ali = [11, 22, 33]
pickle.dump(ali, open('db', 'ab'))

result = pickle.load(open('db', 'r'))
print(result)

2. time模块
import time
import datetime

print(time.time())  # 返回当前系统时间戳
print(time.ctime())  # 输出Tue Jan 26 18:23:48 2016 ,当前系统时间
print(time.ctime(time.time() - 86640))  # 将时间戳转为字符串格式
print(time.gmtime(time.time() - 86640))  # 将时间戳转换成struct_time格式
print(time.localtime(time.time() - 86640))  # 将时间戳转换成struct_time格式,但返回 的本地时间
print(time.mktime(time.localtime()))  # 与time.localtime()功能相反,将struct_time格式转回成时间戳格式
time.sleep(4)  # sleep等待
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))  # 将struct_time格式转成指定的字符串格式
print(time.strptime("2016-06-05", "%Y-%m-%d"))  # 将字符串格式转换成struct_time格式

# datetime module
print(datetime.date.today())  # 输出格式2016-01-26
print(datetime.date.fromtimestamp(time.time() - 864400))  # 2016-01-16 将时间戳转成日期格式
current_time = datetime.datetime.now()  #
print(current_time)  # 输出2016-01-26 19:04:30.335935
print(current_time.timetuple())  # 返回struct_time格式

# datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])
print(current_time.replace(2014, 9, 12))  # 输出2014-09-12 19:06:24.074900,返回当前时间,但指定的值将被替换

str_to_date = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")  # 将字符串转换成日期格式
print(str_to_date)
new_date = datetime.datetime.now() + datetime.timedelta(days=10)  # 比现在加10天
print(new_date)
new_date = datetime.datetime.now() + datetime.timedelta(days=-10)  # 比现在减10天
print(new_date)
new_date = datetime.datetime.now() + datetime.timedelta(hours=-10)  # 比现在减10小时
print(new_date)
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120)  # 比现在+120s
print(new_date)

time_obj = current_time.replace(2015, 5)
print(current_time > time_obj)  # 时间比较
print(current_time == time_obj)

3. logging模块
很多程序都有记录日志的需求，并且日志中包含的信息即有正常的程序访问日志，还可能有错误、警告等信息输出，python的logging模块提供了标准的日志接口，你可以通过它存储各种格式的日志，logging的日志可以分为 debug(), info(), warning(), error() and critical() 5个级别，下面我们看一下怎么用。

用于便捷记录日志且线程安全的模块
import logging

logging.warning("user [admin] attempted wrong password more than 3 times")
logging.critical("server is down")

logging.basicConfig(filename='log.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S %p',
                    level=10)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10,'log')

对应等级:
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
"""




"""
* sys
用于提供对Python解释器相关的操作：
sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.stdin          输入相关
sys.stdout         输出相关
sys.stderror       错误相关
"""

# 例子*进度百分比*
# import sys
# import time
#
#
# def view_bar(num, total):
#     rate = float(num) / float(total)
#     rate_num = int(rate * 100)
#     r = '\r%d%%' % (rate_num,)
#     sys.stdout.write(r)
#     sys.stdout.flush()
#
#
# if __name__ == '__main__':
#     for i in range(0, 101):
#         time.sleep(0.1)
#         view_bar(i, 100)


# 第三方模块
"""
1. requests 模块
"""
# Requests 是使用 Apache2 Licensed 许可证的 基于Python开发的HTTP 库，其在Python内置模块的基础上进行了高度的封装，从而使得Pythoner进行网络请求时，变得美好了许多，使用Requests可以轻而易举的完成浏览器可有的任何操作。
"""
# pip3 install requests
# source install
    # python3 setup.py install
"""

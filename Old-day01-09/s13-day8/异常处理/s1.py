#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

1、# 基本异常处理

while True:
    num1 = input('num1:')
    num2 = input('num2:')
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
    except Exception as ex:  # Exception捕获所有异常
        print(ex)  # str方法
    else:
        print(result)

2、异常种类

python中的异常种类非常多，每个异常专门用于处理某一项异常！！！


AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的

ArithmeticError
AssertionError
AttributeError
BaseException
BufferError
BytesWarning
DeprecationWarning
EnvironmentError
EOFError
Exception
FloatingPointError
FutureWarning
GeneratorExit
ImportError
ImportWarning
IndentationError
IndexError
IOError
KeyboardInterrupt
KeyError
LookupError
MemoryError
NameError
NotImplementedError
OSError
OverflowError
PendingDeprecationWarning
ReferenceError
RuntimeError
RuntimeWarning
StandardError
StopIteration
SyntaxError
SyntaxWarning
SystemError
SystemExit
TabError
TypeError
UnboundLocalError
UnicodeDecodeError
UnicodeEncodeError
UnicodeError
UnicodeTranslateError
UnicodeWarning
UserWarning
ValueError
Warning
ZeroDivisionError

dic = ["wupeiqi", 'alex']
try:
    dic[10]
except IndexError, e:
    print e

dic = {'k1':'v1'}
try:
    dic['k20']
except KeyError, e:
    print e

s1 = 'test'
try:
    int(s1)
except ValueError, e:
    print e
对于上述实例，异常类只能用来处理指定的异常情况，如果非指定异常则无法处理。
# 未捕获到异常，程序直接报错

s1 = 'test'
try:
    int(s1)
except IndexError,e:
    print e
所以，写程序时需要考虑到try代码块中可能出现的任意异常，可以这样写：

s1 = 'test'
try:
    int(s1)
except IndexError,e:
    print e
except KeyError,e:
    print e
except ValueError,e:
    print e
万能异常 在python的异常中，有一个万能异常：Exception，他可以捕获任意异常，即：
s1 = 'test'
try:
    int(s1)
except Exception,e:
    print e
接下来你可能要问了，既然有这个万能异常，其他异常是不是就可以忽略了！

答：当然不是，对于特殊处理或提醒的异常需要先定义，最后定义Exception来确保程序正常运行。
s1 = 'test'
try:
    int(s1)
except KeyError,e:
    print '键错误'
except IndexError,e:
    print '索引错误'
except Exception, e:
    print '错误'
3、异常其他结构
try:
    # 主代码块
    pass
except KeyError,e:
    # 异常时，执行该块
    pass
else:
    # 主代码块执行完，执行该块
    pass
finally:
    # 无论异常与否，最终执行该块
    pass
4、主动触发异常
try:
    raise Exception('错误了。。。')
except Exception,e:
    print e
else:
    pass
finally:
    pass
5、自定义异常
class WupeiqiException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise WupeiqiException('我的异常')
except WupeiqiException,e:
    print e
6、断言
# assert 条件

assert 1 == 1

assert 1 == 2


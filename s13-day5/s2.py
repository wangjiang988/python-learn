#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 字符串格式化
# http://www.cnblogs.com/wupeiqi/articles/5484747.html

# 之前常用%s,%d ,占位符来讲

# %分号方式
"""
%[(name)][flags][width].[precision]typecode

(name)      可选，用于选择指定的key
flags          可选，可供选择的值有:
+       右对齐；正数前加正好，负数前加负号；
-        左对齐；正数前无符号，负数前加负号；
空格    右对齐；正数前加空格，负数前加负号；
0        右对齐；正数前无符号，负数前加负号；用0填充空白处
width         可选，占有宽度
.precision   可选，小数点后保留的位数
typecode    必选
s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
r，获取传入对象的__repr__方法的返回值，并将其格式化到指定位置
c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
o，将整数转换成 八  进制表示，并将其格式化到指定位置
x，将整数转换成十六进制表示，并将其格式化到指定位置
d，将整数、浮点数转换成 十 进制表示，并将其格式化到指定位置
e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
F，同上
g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
G，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）
%，当字符串中存在格式化标志时，需要用 %%表示一个百分号
注：Python中百分号格式化是不存在自动将整数转换成二进制表示的方式
"""

# name:
string = "\033[34;1m你好,%(name)s to %(age)d" % {'name': 'admin', 'age': 18}
print(string)

# flag,width
string = "你好,%(name)-10s to %(age)+10d" % {'name': 'admin', 'age': 18}
print(string)

# .precision
string = "你好,%(name)-10s to %(age)+10d %(p).2f" % {'name': 'admin', 'age': 18, 'p': 3.1415926}
print(string)

# typecode
string = "Convert: 65的unicode值为: %c **** 15的八进制为: %o **** 15的十六进制为: %x" % (65, 15, 15)
print(string)

# 当格式化时,字符串中出现占位符%s, %d,需要用%%输出%
string = "Welcome to %s" % "BeiJing"
print(string)

# 常用字符串格式化
eg1 = "My name is %s" % "Admin"
print(eg1)

eg2 = "My name is %s, i'm %d" % ("Admin", 18)
print(eg2)

eg3 = "My name is %(name)s i'm %(age)d" % {"name": "admin", "age": 18}
print(eg3)

eg4 = "percent %.2f" % 99.97623
print(eg4)

eg5 = "pi = %(pi).6f" % {"pi": 3.1415926535898}
print(eg5)

eg6 = "pi = %(pi).6f %%" % {"pi": 3.1415926535898}
print(eg6)

# Format方式

"""
[[fill]align][sign][#][0][width][,][.precision][type]

fill           【可选】空白处填充的字符
align        【可选】对齐方式（需配合width使用）
<，内容左对齐
>，内容右对齐(默认)
＝，内容右对齐，将符号放置在填充字符的左侧，且只对数字类型有效。 即使：符号+填充物+数字
^，内容居中
sign         【可选】有无符号数字
+，正号加正，负号加负；
 -，正号不变，负号加负；
空格 ，正号空格，负号加负；
#            【可选】对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示
，            【可选】为数字添加分隔符，如：1,000,000
width       【可选】格式化位所占宽度
.precision 【可选】小数位保留精度
type         【可选】格式化类型
传入” 字符串类型 “的参数
s，格式化字符串类型数据
空白，未指定类型，则默认是None，同s
传入“ 整数类型 ”的参数
b，将10进制整数自动转换成2进制表示然后格式化
c，将10进制整数自动转换为其对应的unicode字符
d，十进制整数
o，将10进制整数自动转换成8进制表示然后格式化；
x，将10进制整数自动转换成16进制表示然后格式化（小写x）
X，将10进制整数自动转换成16进制表示然后格式化（大写X）
传入“ 浮点型或小数类型 ”的参数
e， 转换为科学计数法（小写e）表示，然后格式化；
E， 转换为科学计数法（大写E）表示，然后格式化;
f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
F， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
g， 自动在e和f中切换
G， 自动在E和F中切换
%，显示百分比（默认显示小数点后6位）
"""

# 基本用法
string = "string{0}string{0}num{1}".format(" docker ", 185)
print(string)

# fill,align,sign,width
string = "空格填充后的string居中显示为{: ^20s}".format("Docker")
print(string)
string = "*号填充后的string左对齐显示为{:*<20s}".format("Docker")
print(string)
string = "string{: ^20s}, number{:+d}".format("Docker", 100)
print(string)

# .precision
string = "π = {:.5}".format(3.1415926535898)
print(string)

# % 自动转换为%分比的方式再格式化
string = "3.1415926535898的百分比为 = {:.2%}".format(3.1415926535898)
print(string)

# type
string = "15的二进制是: {:b}".format(175)
print(string)

# ** 常用字符串格式化
eg1 = "My name is {}, i'm {}, Hello, {}".format("seven", 18, 'admin')
print(eg1)

# ** 列表方式传参 = *args
eg2 = "My name is {}, i'm {}, Hello, {}".format(*["seven", 18, 'admin'])
print(eg2)

eg3 = "My name is {0}, i'm {1}, really {0}".format("seven", 18)
print(eg3)

# 索引方式传参
eg4 = "My name is {0}, i'm {1}, really {0}".format(*["seven", 18])
print(eg4)

# ** 指定名称传参
eg5 = "My name is {name}, i'm {age}, really {name}".format(name="seven", age=18)
print(eg5)

# ** 字典方式传参 = **kwargs
eg6 = "My name is {name}, i'm {age}, really {name}".format(**{"name": "seven", "age": 18})
print(eg6)

# 支持索引套索引
eg7 = "number1 {0[0]}, number2 {0[1]}, number3 {0[2]}".format([1, 2, 3], [11, 22, 33])
print(eg7)

eg8 = "My name is {:s}, i'm {:d}, money {:f}".format("seven", 18, 88888.1)
print(eg8)

eg9 = "My name is {:s}, i'm {:d}".format(*["seven", 18])
print(eg9)

eg10 = "My name is {name:s}, i'm {age:d}".format(name="seven", age=18)
print(eg10)

eg11 = "My name is {name:s}, i'm {age:d}".format(**{"name": "seven", "age": 18})
print(eg11)

eg12 = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(eg12)

# **
eg13 = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(eg13)

# **
eg14 = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
print(eg14)

eg15 = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}\033[0m".format(num=15)
print(eg15)

# 生成器和迭代器
# 生成器
# 一个函数调用时返回一个迭代器，那这个函数就叫做生成器（generator）；如果函数中包含yield语法，那这个函数就会变成生成器；
li = [11, 22, 33, 44, 55]
result = filter(lambda a: a > 33, li)
print(result)  # 具有生成指定条件数据的能力的一个对象
for i in result:
    print(i)

# 使用函数创造生成器


def func():  # func就是一个生成器
    print("First")
    yield 1  # yield保存上一次执行的位置
    print("Second")
    yield 2
    print("Third")
    yield 3
# 上述代码中：func是函数称为生成器，当执行此函数func()时会得到一个迭代器。
ret = func()
# print(ret)
n1 = ret.__next__()  # 取值,进入函数找到yield,获取yield后面的数据
print(n1)
n2 = ret.__next__()  # 取值,进入函数找到yield,获取yield后面的数据
print(n2)
n3 = ret.__next__()  # 取值,进入函数找到yield,获取yield后面的数据
print(n3)
# for i in ret:
#     print(i)  # 第一次循环拿到print,第二次循环从print的位置继续往下执行拿到1,依次往下执行

# 实例
# 通过yield自定义生成器,生成0-9的数字


def myrange(args):
    start = 0
    while True:
        if start > args:
            return
        yield start
        start += 1

ret = myrange(9)
num = ret.__next__()
print(num)
for i in ret:  # 迭代器
    print(i)

# 迭代器 , 可被迭代的对象就是迭代器, for调用等于使用next一直往下查找
"""
迭代器是访问集合元素的一种方式。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退，不过这也没什么，因为人们很少在迭代途中往后退。另外，迭代器的一大优点是不要求事先准备好整个迭代过程中所有的元素。迭代器仅仅在迭代到某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁。这个特点使得它特别适合用于遍历一些巨大的或是无限的集合，比如几个G的文件

特点：

访问者不需要关心迭代器内部的结构，仅需通过next()方法不断去取下一个内容
不能随机访问集合中的某个值 ，只能从头到尾依次访问
访问到一半时不能往回退
便于循环比较大的数据集合，节省内存
"""

# 递归
# 程序本身自己调用自己称之为递归，类似于俄罗斯套娃，体现在代码中：用户执行最外（N）层函数，最外侧调用N-1层函数，N-1层函数调用N-2层函数...
# 函数无返回值返回None,有返回值就返回传值


def func(n):
    n += 1
    if n >= 4:
        return "End"
    return func(n)

r = func(1)
print(r)


# 利用递归得到1*2*3*4*5*6*7
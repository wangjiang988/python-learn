#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

"""
1. sys模块
sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.stdout.write('please:')
sys.stdout.flush    将我们写入缓冲区的内容刷到终端上，而不是清空，而打印的内容，都是先写入到缓冲区，然后再在终端显示的。(立即让内容显示出来的效果)
val = sys.stdin.readline()[:-1]

2. os 用于提供系统级别的操作
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
os.curdir  返回当前目录: ('.')
os.pardir  获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep    输出用于分割文件路径的字符串
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  运行shell命令，直接显示
os.environ  获取系统环境变量
os.path.abspath(path)  返回path规范化的绝对路径
os.path.split(path)  将path分割成目录和文件名二元组返回
os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间

更多介绍: https://docs.python.org/2/library/os.html?highlight=os#module-os

3. hashlib
用于加密相关的操作，代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法

import hashlib

# ######## md5 ########

hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()

# ######## sha1 ########

hash = hashlib.sha1()
hash.update('admin')
print hash.hexdigest()

# ######## sha256 ########

hash = hashlib.sha256()
hash.update('admin')
print hash.hexdigest()


# ######## sha384 ########

hash = hashlib.sha384()
hash.update('admin')
print hash.hexdigest()

# ######## sha512 ########

hash = hashlib.sha512()
hash.update('admin')
print hash.hexdigest()

以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。
import hashlib

# ######## md5 ########

hash = hashlib.md5('898oaFs09f')
hash.update('admin')
print hash.hexdigest()
还不够吊？python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 再进行处理然后再加密
import hmac
h = hmac.new('wueiqi')
h.update('hellowo')
print h.hexdigest()

4. re 正则
re.findall('alex', 'yuanaleSxalexwupeiqi')
2元字符 . ^ $ * + ? {}
. 匹配a-Z的单个任意字符
re.findall('al.x', 'yuanaleSxalexwupeiqi')
^ 匹配以...开头
re.findall('^al.x', 'yuanaleSxalexwupeiqi')
$ 匹配以...结尾
re.findall('^al.x', 'yuanaleSxalexwupeiqi')
* + ? {} 重复
* *前面的字符匹配0到多次
re.findall('^al.*x', 'yuanaleSxalexwupeiqi')
+ +1到多次
re.findall('^al.+x', 'yuanaleSxalexwupeiqi')
re.findall('^al.?x', 'yuanaleSxalexwupeiqi')
re.findall('^al.{1.5}x', 'yuanaleSxalexwupeiqi')
[]
re.findall('a[bc]d', 'abd')
re.findall('a[a-z]d', 'abd')
re.findall('a[a-z]+d', 'abugd')

在[]中, - 代表范围, ^ 代表非, \
re.findall('a[^f]d', 'add')

re.match('com', 'www.baidu.com').group()
re.search('com', 'www.runcomoob')
re.split('\d+', 'one1two2three3')
re.compile()
http://www.cnblogs.com/wupeiqi/articles/4963027.html

作业:
-计算器-

"""

# 例子*进度百分比*
import sys
import time


def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r[%s]%d%%' % ("#" * num, rate_num, )  # \r表示重新回到当前行的首个位置
    sys.stdout.write(r)  # 输出
    sys.stdout.flush()  # 输出清空


if __name__ == '__main__':
    for i in range(0, 101):
        time.sleep(0.1)
        view_bar(i, 100)

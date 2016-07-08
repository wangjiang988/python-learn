#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

"""
可以执行shell命令的相关模块和函数有：

os.system
os.spawn*
os.popen*          --废弃
popen2.*           --废弃
commands.*      --废弃，3.x中被移除

import commands

result = commands.getoutput('cmd')
result = commands.getstatus('cmd')
result = commands.getstatusoutput('cmd')
以上执行shell命令的相关的模块和函数的功能均在 subprocess 模块中实现，并提供了更丰富的功能。
"""

import subprocess

# call 执行命令
ret = subprocess.call(["ls", "-l"], shell=False)
print(ret)
ret = subprocess.call("ls -l", shell=True)
print(ret)

# check_call 执行命令，如果执行状态码是 0 ，则返回0，否则抛异常

ret = subprocess.check_call(["ls", "-l"])
print(ret)
ret = subprocess.check_call("exit", shell=True)
print(ret)
# check_output 执行命令，如果状态码是 0 ，则返回执行结果，否则抛异常

print(subprocess.check_output(["echo", "Hello World!"]))
print(subprocess.check_output("exit", shell=True))

print(subprocess.getoutput("ls -l"))

# subprocess.Popen(...) 用于执行复杂的系统命令

"""
参数：

args：shell命令，可以是字符串或者序列类型（如：list，元组）
bufsize：指定缓冲。0 无缓冲,1 行缓冲,其他 缓冲区大小,负值 系统缓冲
stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
preexec_fn：只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。
所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
shell：同上
cwd：用于设置子进程的当前目录
env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
universal_newlines：不同系统的换行符不同，True -> 同意使用 \n
startupinfo与createionflags只在windows下有效
将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等
"""

ret1 = subprocess.Popen(["mkdir","t1"])
ret2 = subprocess.Popen("mkdir t2", shell=True)

"""
终端输入的命令分为两种：

输入即可得到输出，如：ifconfig
输入进行某环境，依赖再输入，如：python
"""

obj = subprocess.Popen("mkdir t3", shell=True, cwd='/home/dev',)

# 复杂写法

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)

# 简单写法
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")

out_error_list = obj.communicate()  # 去错误管道及输出管道里面获取内容
print(out_error_list)

# 简单命令执行
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       universal_newlines=True)
out_error_list = obj.communicate('print("hello")')
print(out_error_list)


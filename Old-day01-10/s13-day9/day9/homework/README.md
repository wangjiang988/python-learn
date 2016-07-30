## 目录
* [背景介绍](#背景介绍)
* [项目介绍](#程序功能介绍)
* [使用说明](#使用说明)
   * [获取代码](#获取代码)
   * [目录介绍](#目录介绍)
* [其他](#其他)
   

## 背景介绍

> Socket实现Ftp客户端和服务端

## 程序功能介绍

开发一个支持多用户在线的FTP程序

要求：
* 用户加密认证
* 允许同时多用户登录
* 每个用户有自己的家目录 ，且只能访问自己的家目录
* 对用户进行磁盘配额，每个用户的可用空间不同
* 允许用户在ftp server上随意切换目录
* 允许用户查看当前目录下文件
* 允许上传和下载文件，保证文件一致性
* 文件传输过程中显示进度条
* 附加功能：支持文件的断点续传

## 使用说明

### 获取代码

[项目地址](<https://github.com/smartczm/python-learn/tree/master/s13-day9/day9>)

### 环境需求 

`Python版本 >= Python3.0`

### 目录介绍

```txt
day9  # 顶级目录
└── homework  # 主目录
    ├── README.md  # readme文件
    ├── ftpclient  # ftp客户端主目录
    │   ├── bin
    │   │   └── ftp_client.py  # ftp客户端运行文件
    │   ├── conf
    │   │   └── conf.py  # 配置文件
    │   ├── core
    │   │   ├── client.py  # 客户端核心文件
    │   │   └── users.py  # 用户相关文件
    │   └── lib
    │       ├── commons.py  # 库文件
    │       └── progressbar.py  # 进度条模块
    └── ftpserver  # ftp服务端主目录
        ├── bin
        │   └── ftp_server.py  # ftp服务端运行文件
        ├── conf
        │   └── conf.py  # 配置文件
        ├── core
        │   ├── server.py  # 服务端核心文件
        │   └── users.py  # 用户相关文件
        ├── database
        │   └── userlist  # 用户信息
        ├── home
        │   ├── chenliang  # ftp个人家目录
        │   └── guest  # 匿名用户目录
        │       └── test  # 测试文件
        ├── lib
        │   ├── commons.py  # 库文件
        │   └── progressbar.py  # 进度条文件
        └── logs
            └── ftp_server.log  # 日志文件

16 directories, 17 files

```

### QuickStart

```shell
# python3 ftp_server.py
FtpServer is running...

# python3 ftp_client.py
欢迎使用Myftp
 输入help可查看帮助信息
guest:>> help

--------------------------------------------------------------------------------------------
欢迎使用Myftp
--------------------------------------------------------------------------------------------

      ls:  用于显示当前目录下文件或文件详细信息，格式：ls
     get:  用于下载文件，格式：get path/to/filename [dst/path/to/]
     put:  用于上传文件，格式：put path/to/filename，说明：path/to/格式要求同cd命令
      rm:  用于删除文件或目录，格式：rm path/to[/filename]
      cd:  用于切换服务端目录，格式：cd path/to/
    auth:  用户认证，格式：auth，然后根据提示输入用户名及密码
guest:>> ls
total 0
drwxr-xr-x  3 ChenLiang  staff  102  7  9 00:55 .
drwxr-xr-x  4 ChenLiang  staff  136  7  8 23:49 ..
-rw-r--r--  1 ChenLiang  staff    0  7  9 00:55 test

guest:>> rm test
操作执行成功
guest:>> ls
total 0
drwxr-xr-x  2 ChenLiang  staff   68  7  9 00:56 .
drwxr-xr-x  4 ChenLiang  staff  136  7  8 23:49 ..

```

## 其他
 
时间仓促，功能简陋，望您包涵。您有任意的意见和建议，欢迎随意与我沟通,联系方式：
* Email: <chenlerry@gmail.com>
* QQ:554248852
* Blog:[SmartCZM](http://www.smartczm.com)
项目的Bug和改进点，可以email的方式直接提交给我 thk.

[Python Day9](<https://www.smartczm.com/python_day9.html>)

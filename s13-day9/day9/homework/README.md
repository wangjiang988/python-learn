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

[项目地址](<https://github.com/smartczm/python-learn/tree/master/s13-day5/day5>)

### 环境需求 

`Python版本 >= Python3.0`

### 目录介绍

```txt
day9
├── README.md
└── homework
    ├── ftpclient
    │   ├── bin
    │   │   └── ftp_client.py
    │   ├── conf
    │   │   └── conf.py
    │   ├── core
    │   │   ├── client.py
    │   │   └── users.py
    │   └── lib
    │       ├── commons.py
    │       └── progressbar.py
    ├── ftpserver
    │   ├── bin
    │   │   └── ftp_server.py
    │   ├── conf
    │   │   └── conf.py
    │   ├── core
    │   │   ├── server.py
    │   │   └── users.py
    │   ├── database
    │   │   └── userlist
    │   ├── home
    │   │   ├── chenliang
    │   │   └── guest
    │   │       ├── id_rsa.key
    │   │       └── test
    │   ├── lib
    │   │   ├── commons.py
    │   │   └── progressbar.py
    │   └── logs
    │       └── ftp_server.log
    └── readme.txt

16 directories, 18 files
```

### QuickStart

```shell
# sh bin/atm_admin.sh start  # 后台管理启动
用户名（输入quit退出）：admin
密码: 123
认证成功，按任意键继续

**********************************
* 欢迎来到768银行后台系统        *
* Version: 1.0                   *
* admin 您好                     *
**********************************
1、 添加账户
2、 查看并管理账户
3、 退出系统
请选择：

# sh bin/atm_client.sh start  # 后台客户端启动
卡号（输入quit退出认证）: 123456789
密码: 123
认证成功，按任意键继续

**********************************
* 欢迎来到768银行                *
* Version: 1.0                   *
* chenliang 您好                 *
* 当前余额: 15000.0              *
**********************************
1、 查看详细信息
2、 查看账单
3、 提现
4、 还款
5、 同行转账
6、 查看消费流水
7、 修改密码
8、 退出
请选择：

# sh bin/shopping.sh start  # 购物程序启动

**********************************
* 欢迎来到768购物中心            *
* Version: 1.0                   *
* 游客 您好                      *
**********************************
1、 购物
2、 注册
3、 登录
4、 注销
5、 修改密码
6、 查看购物车
7、 退出
请选择：

# sh bin/crontab_add.sh   # 计划任务添加
```

## 其他
 
时间仓促，功能简陋，望您包涵。您有任意的意见和建议，欢迎随意与我沟通,联系方式：
* Email: <chenlerry@gmail.com>
* QQ:554248852
* Blog:[SmartCZM](http://www.smartczm.com)
项目的Bug和改进点，可以email的方式直接提交给我 thk.

[Python Day5 Blog01](<https://www.smartczm.com/python_day5_01.html>)
[Python Day5 Blog02](<https://www.smartczm.com/python_day5_02.html>)

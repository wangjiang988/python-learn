## 目录
* [背景介绍](#背景介绍)
* [项目介绍](#程序功能介绍)
* [使用说明](#使用说明)
   * [获取代码](#获取代码)
   * [目录介绍](#目录介绍)
* [其他](#其他)
   

## 背景介绍

> RabbitMQ RPC实现,及通过SQLAlchemy+Paramiko操作远程主机

## 使用说明

### 获取代码

[项目地址](<https://github.com/smartczm/python-learn/tree/master/s13-day13/day13>)

### 环境需求 

`Python版本 >= Python3.0`

### 目录介绍

```txt
day13
├── README.md  # README文件
└── homework  # 主程序目录
    ├── conf
    │   ├── auth.py  # 调用方法文件
    │   └── conf.py  # 配置文件
    ├── lib
    │   ├── commons.py  # 库文件
    ├── manager.py  # 主程序
    │   ├── cmd_def.py  # 命令行参数条用
    │   ├── db_conn.py  # 数据库连接信息
    │   ├── hm_schema.py  # 数据库结构模块
    │   ├── interactive.py  # 交互式操作模块
    │   ├── log_model.py  # 日志模块
    │   └── terminal.py  # 终端模块
    └── templates  # 模板文件目录
        └── example  # 批量导入目录
            ├── groups.json  # 组
            ├── hosts.json  # 主机
            ├── hostusers.json  # 主机用户
            └── users.json  # 堡垒机用户
```

### QuickStart

```shell
1、模块安装：
需安装第三方的paramiko、sqlalchemy、sqlalchemy_util库
pip3 install paramiko sqlalchemy sqlalchemy-utils

2、Linux：
直接执行# python3 manager.py [commend [otpions]] 或#./manager.py [commend [otpions]]（需要给主程序文件添加可执行权限）

3、Windows：暂不支持Windows

4、使用方法
初始化配置：用于第一次运行堡垒机程序，创建数据库、数据库表批量导入数据

- 创建数据库、数据库用户，以MySQL为例
mysql> create database chenliang charset=utf8;

mysql> grant all on chenliang.* to root@'%' identified by '123456';
Query OK, 0 rows affected (0.03 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.02 sec)

- 注意: 需要先配置数据库链接，修改主配置文件DBS和DB字段

- 初始化数据库表
$ python3 manager.py init_database
数据库初始化...

# Check
MariaDB [chenliang]> show tables;
+-------------------------+
| Tables_in_chenliang     |
+-------------------------+
| audit_log               |
| group                   |
| host                    |
| host_user               |
| hostuser_to_group       |
| user_profile            |
| userprofile_to_group    |
| userprofile_to_hostuser |
+-------------------------+

- 导入主机列表
    - 批量导入，（通过-f选项指定文件目录）
    $ python3 manager.py import_hosts -f templates/example/hosts.json
    
- 导入远端主机用户列表
    - 批量导入，（通过-f选项指定文件目录）
    $ python3 manager.py import_remoteusers -f templates/example/hostusers.json
    
- 按照同样的操作方式来导入groups,然后导入users
    $ python3 manager.py import_groups -f templates/example/groups.json
    $ python3 manager.py import_users -f templates/example/users.json

PS：导入顺序不能颠倒，需要严格按照流程。至此，初始化配置工作完成。

启动并连接服务器
$ python3 manager.py start                                                1 ↵  ✖ ✹ ✭master
Username: chenliang
Password:
------------------ Welcome tp login Jumpserver ------------------
主机信息: (1)
   1.	 root@web-001(172.16.3.250)
组信息: (1)
   2.	 cluster
chenliang (q)quit>> 2
   1.	 chenliang@cluster-001(172.16.131.129)
(q)quit, (b)break>> 1
Connect remote host [172.16.131.129] as user [chenliang]...
Connect success let's go [chenliang]
[chenliang@centos7 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eno16777728: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 00:0c:29:e0:3b:3d brd ff:ff:ff:ff:ff:ff
    inet 172.16.131.129/24 brd 172.16.131.255 scope global dynamic eno16777728
       valid_lft 1719sec preferred_lft 1719sec
    inet6 fe80::20c:29ff:fee0:3b3d/64 scope link
       valid_lft forever preferred_lft forever
       
[chenliang@centos7 ~]$ exit
登出

*** EOF
------------------ Welcome tp login Jumpserver ------------------
主机信息: (1)
   1.	 root@web-001(172.16.3.250)
组信息: (1)
   2.	 cluster
chenliang (q)quit>> q
```

## 其他
 
时间仓促，功能简陋，望您包涵。您有任意的意见和建议，欢迎随意与我沟通,联系方式：
* Email: <chenlerry@gmail.com>
* QQ:554248852
* Blog:[SmartCZM](http://www.smartczm.com)
项目的Bug和改进点，可以email的方式直接提交给我 thk.

[Python Day13](<https://www.smartczm.com/python_day13.html>)

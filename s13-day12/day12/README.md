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

[项目地址](<https://github.com/smartczm/python-learn/tree/master/s13-day12/day12>)

### 环境需求 

`Python版本 >= Python3.0`

### 目录介绍

```txt
day12   - 主目录
├── README.md  - README文件
└── homework
    ├── alchemy
    │   ├── exec.py  - 远程执行程序
    │   └── sql.py  - sql程序
    └── rpc
        ├── demo1  - 官方Demo
        │   ├── rpc_client.py
        │   └── rpc_server.py
        └── demo2  - 远端执行命令
            ├── bin  - 主程序运行目录
            │   ├── client.py  - 客户端运行程序
            │   └── server.py  - 服务端运行程序
            ├── conf  - 配置文件目录
            │   └── conf.py  - 主配置文件
            ├── core  - 核心文件目录
            │   ├── rpc_client.py  - 客户端主程序
            │   └── rpc_server.py  - 服务端主程序
            ├── lib - 库文件目录
            │   └── commons.py  - 库文件
            └── logs - 日志目录
                ├── client.log  - 客户端日志
                └── server.log  - 服务端日志
```

### QuickStart

```shell
1、Linux：
        1)Server端（执行命令端）：直接执行# python3 server.py 或#./server.py（需要给主程序文件添加可执行权限）
        2)Client端（发送命令端）：直接执行# python3 client.py [command]或#./client.py（需要给主程序文件添加可执行权限）
2、Windows：暂不支持Windows
        1)Agent端：直接执行# python3 server.py
        2)Client端：直接执行# python client.py [command]
```

## 其他
 
时间仓促，功能简陋，望您包涵。您有任意的意见和建议，欢迎随意与我沟通,联系方式：
* Email: <chenlerry@gmail.com>
* QQ:554248852
* Blog:[SmartCZM](http://www.smartczm.com)
项目的Bug和改进点，可以email的方式直接提交给我 thk.

[Python Day12](<https://www.smartczm.com/python_day12.html>)

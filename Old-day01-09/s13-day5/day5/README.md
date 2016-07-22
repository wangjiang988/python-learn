## 目录
* [背景介绍](#背景介绍)
* [项目介绍](#程序功能介绍)
* [使用说明](#使用说明)
   * [获取代码](#获取代码)
   * [目录介绍](#目录介绍)
* [其他](#其他)
   

## 背景介绍

> ATM+购物商城程序实现

## 程序功能介绍

* 额度 15000或自定义
* 实现购物商城，买东西加入 购物车，调用信用卡接口结账
* 可以提现，手续费5%
* 每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计息
* 支持多账户登录
* 支持账户间转账
* 记录每月日常消费流水
* 提供还款接口
* ATM记录操作日志
* 提供管理接口，包括添加账户、用户额度，冻结账户等

## 使用说明

### 获取代码

[项目地址](<https://github.com/smartczm/python-learn/tree/master/s13-day5/day5>)

### 环境需求 

`Python版本 >= Python3.0`

### 目录介绍

```txt
day5  # Project主目录
├── README.md  # README介绍文件 
├── homework  # 程序主目录
│   ├── bin  # 程序运行bin目录
│   │   ├── atm_admin.sh  # atm后台管理运行脚本
│   │   ├── atm_client.sh  # atm客户端运行脚本
│   │   ├── crontab_add.sh  # 计划任务执行脚本
│   │   └── shopping.sh  # 购物商城运行脚本
│   ├── dbs  # 数据目录
│   │   ├── list.db  # 商品列表
│   │   ├── user_record.db  # 用户消费购物记录
│   │   └── userinfo.db  # 用户个人信息
│   ├── libs  # 库文件目录
│   │   └── commons.py  # 自定义各种通用库文件
│   ├── log  # 日志如来
│   │   ├── atm_history.log  # atm相关操作日志
│   │   └── shopping_history.log  # 购物相关历史记录
│   ├── model  # 主模块模块
│   │   ├── account.py  # 账户管理
│   │   ├── atm.py  # atm相关
│   │   ├── customer.py  # 用户操作
│   │   ├── goods.py  # 商品获取
│   │   ├── shopping.py  # 购物相关
│   └── src  # 核心程序运行目录
│       ├── atm_admin.py  # ATM管理程序
│       ├── atm_client.py  # ATM客户端程序
│       ├── atm_crontab.py  # ATM定时任务程序
│       ├── conf.py  # 配置文件
│       └── shopping.py  # 商城主程序
└── atm-shopping.jpg  # 逻辑图
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


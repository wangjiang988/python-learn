## 目录
* [背景介绍](#背景介绍)
* [项目介绍](#程序功能介绍)
* [使用说明](#使用说明)
   * [获取代码](#获取代码)
   * [目录介绍](#目录介绍)
* [其他](#其他)
   

## 背景介绍

> 公司有haproxy配置文件，希望通过python程序可以对ha配置文件进行增删改，不再是以往的打开文件进行直接操作

## 程序功能介绍

> haproxy配置文件更改

* 获取记录
    * 通过输入backend相关的域名来获取backend下面的条目记录
* 增加记录
    * 通过输入固定条目:'{"backend":"abc.oldboy.org","record":{"server":"100.1.7.9","weight":"20","maxconn":"3000"}}'来将backend或者record下面的value信息加入到配置文件中
* 删除记录
    * 通过输入固定条目:'{"backend":"abc.oldboy.org","record":{"server":"100.1.7.9","weight":"20","maxconn":"3000"}}'来将backend或者record下面的value信息从配置文件中删除
* 恢复初始配置
    * 通过备份的配置文件版本信息来还原操作

## 使用说明

### 获取代码

[项目地址](<https://github.com/smartczm/python-learn/tree/master/s13-day3/day3>)

### 环境需求 

`Python版本 >= Python3.0`

### 目录介绍

```txt
day3  # 项目主目录    
├── README.md   # README文件    
└── index    # 程序主目录    
    ├── file_operation.py  # 程序文件    
    └── haproxy.cfg  # 配置文件
    
1 directory, 3 files
```

### QuickStart

```shell
chmod +x file_operation.py ; ./file_operation.py     
or    
 python3 file_operation.py
```

## 其他
 
时间仓促，功能简陋，望您包涵。您有任意的意见和建议，欢迎随意与我沟通,联系方式：
* Email: <chenlerry@gmail.com>
* QQ:554248852
* Blog:[SmartCZM](http://www.smartczm.com)
项目的Bug和改进点，可以email的方式直接提交给我 thk.

[Python Day3 Blog](<http://www.smartczm.com/python_day3.html>)
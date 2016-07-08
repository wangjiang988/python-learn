## 目录
* [背景介绍](#背景介绍)
* [项目介绍](#程序功能介绍)
* [使用说明](#使用说明)
   * [获取代码](#获取代码)
   * [目录介绍](#目录介绍)
* [其他](#其他)
   

## 背景介绍

> 通过re编写一个计算器

## 程序功能介绍

> 计算器

```python
python3 calculator.py
计算公式案例: 1-2*-30/-12*(-20+200*-3/-200*-300-100)
请输入你要计算的公式: 1-2*-30/-12*(-20+200*-3/-200*-300-100*(50-100*30))

# 处理第一次括号中表达式的结果
before： 1-2*-30/-12*(-20+200*-3/-200*-300-100*(50-100*30))
50-100*30=-2950.0
after： 1-2*-30/-12*(-20+200*-3/-200*-300-100*-2950.0)
========== 上一次计算结束 ==========

# 处理第二次括号中表达式的结果
before： 1-2*-30/-12*(-20+200*-3/-200*-300-100*-2950.0)
-20+200*-3/-200*-300-100*-2950.0=294080.0
after： 1-2*-30/-12*294080.0
========== 上一次计算结束 ==========

# 整体结果计算
-1470399.0
```

## 使用说明

### 获取代码

[项目地址](<https://github.com/smartczm/python-learn/tree/master/s13-day6/day6>)

### 环境需求 

`Python版本 >= Python3.0`

### 目录介绍

```txt
day6  # 项目主目录
├── README.md  # README文件
├── calculator.png  # 程序流程图
└── homework  # 程序工作目录
    └── calculator.py  # 主程序 通过re实现计算器
    └── calc.py  # 主程序 通过math\re\eval实现计算器
```

### QuickStart

```shell
chmod +x calculator.py ; ./calculator.py
chmod +x calc.py ; ./calc.py 
or    
 python3 calculator.py
 python3 calc.py
```

## 其他
 
时间仓促，功能简陋，望您包涵。您有任意的意见和建议，欢迎随意与我沟通,联系方式：
* Email: <chenlerry@gmail.com>
* QQ:554248852
* Blog:[SmartCZM](http://www.smartczm.com)
项目的Bug和改进点，可以email的方式直接提交给我 thk.

[Python Day6 前半部分](<https://www.smartczm.com/python_day5_02.html>)

[Python Day6 后半部分](<https://www.smartczm.com/python_day6.html>)
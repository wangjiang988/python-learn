## 目录
* [背景介绍](#背景介绍)
* [项目介绍](#程序功能介绍)
* [使用说明](#使用说明)
   * [获取代码](#获取代码)
   * [目录介绍](#目录介绍)
* [其他](#其他)
   

## 背景介绍

> 开发一套选课系统

## 程序功能介绍

> 选课系统

```python
管理员:
    1, 创建老师(爱好, 姓名, 年龄, 资产默认0)
    class Teacher:
        def __init__(self, favor, name, age):
            self.favor = favor
            self.name = name
            self.age = age
            self.asset = 0
        def jiaoxueshigu(self):
            self.asset -= 1
        def jiaqian(self, value):
            self.asset += value
    obj1 = Teacher(...)
    obj2 = Teacher(...)
    [obj1, obj2, obj3]
    pickle.dump([obj1, obj2, obj3], 文件)
    # Teacher 类型
    2, 创建课程
    li = pickle.load([obj1, obj2, obj3])
    li[0]
    class Book:
        def __init__(self, 课程名, 课时费, 负责老师 = li[0])
        def 上课
                返回给学生学习的内容
                负责给老师加钱li[0].gain(课时费)
学生:
    类:
    class Students:
        def __init__(self, 选课)
            选课 = [课程对象]
        def 上课:
            选课
            1, 生物课
                课程对象.上课()
```

## 使用说明

### 获取代码

[项目地址](<https://github.com/smartczm/python-learn/tree/master/s13-day7/day7>)

### 环境需求 

`Python版本 >= Python3.0`

### 目录介绍

```txt
day7  # 项目主目录
├── README.md  # README文件
└── homework  # 程序工作目录
```

### QuickStart

```shell
```

## 其他
 
由于最近单位事情较多,大部分时间都是在单位上班,时间仓促，本次作业只写了博客.
* Email: <chenlerry@gmail.com>
* QQ:554248852
* Blog:[SmartCZM](http://www.smartczm.com)

[Python Day7 前半部分](<https://www.smartczm.com/python_day6.html>)
[Python Day7 前半部分](<https://www.smartczm.com/python_day7.html>)

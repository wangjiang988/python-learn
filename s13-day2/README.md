> 购物车程序

## 介绍

> 用于用户进行商品采购

## 目录结构


```conf
shopping_mall_v1.py - 主程序    
    dump.txt - 商品历史记录    
    lock.txt - 用户锁记录    
    name.txt - 用户列表
```

## 环境需求 `Python版本 >= Python3.0`

## shopping_mall_v1.py功能特性

> 基本功能:    

* 用户启动时输入工资    

* 用户启动程序后打印商品列表    

* 允许用户选择购买商品    

* 允许用户不断的购买各种商品    

* 购买时监测余额是否足够,如果足够直接扣款,否则打印余额不足    

* 允许用户主动退出程序,退出时打印已购商品列表    

> 进阶功能:    

* 允许用户选择购买多少件商品    

* 允许多用户登录,下一次登录后,继续按上次的余额继续购买(可以充值)    

* 允许用户查看之前购买记录(记录要显示商品购买时间)    

* 实现商品列表分级展示，比如    

```txt
第一层菜单： 	
1.	家电类 	
2.	衣服 	
3.	手机类 	
4.	车类 	
    随便选择一个，比如车类，进入第2层 		
    1. BMW X3 33333 		
    2. Audi Q5 33355 		
    3. Pasate  33335
```

* 实现显示已购买商品时， 如果有重复的商品， 不打印多行，而是在一行展示，如

```txt
id	p_name		num		total_price 		
1. TeslaModelS  2 		34242424 		
2. Coffee		2 		60 
```

## Run


```txt
chmod +x shopping_mall_v1.py ; ./shopping_mall_v1.py     
or    
 python3 shopping_mall_v1.py
```

[Python Day2 Blog](<http://www.smartczm.com/python_day2.html>)
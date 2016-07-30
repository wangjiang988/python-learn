#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import pymysql

conn = pymysql.connect(host='172.16.131.129', port=3306, user='chenliang', passwd='123456', db='chenliang')

# 游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
r = cursor.execute("select * from t_account")

result = cursor.fetchone()
print(result)

conn.commit()
cursor.close()
conn.close()


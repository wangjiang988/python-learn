#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


id_db = {
    510824134010130534: {
        'name': "Alex Li",
        'age': 22,
        'addr': 'ShanDong'
    },
    220182143511229843: {
        'name': "Xin Fan",
        'age': 25,
        'addr': 'FengDong'
    },
    220182143511229743: {  # Key必须唯一
        'name': "Da Xin Fan",
        'age': 28,
        'addr': 'FengDong'
    },
}

print(id_db[510824134010130534])  # 取值
id_db[510824134010130534]['name'] = 'Xiao Hu'  # 修改
id_db[510824134010130534]['qq_write'] = '34123223'  # 添加新value
print(id_db[510824134010130534])
# del id_db[510824134010130534]['addr']  # 删除
# pop_remove = id_db[510824134010130534].pop('addr') # 删除
# print(pop_remove)
print(id_db.copy())  # 等于列表的copy
print(id_db)

print(id_db[510824134010130534])
# print(id_db[5108241340101305343])  # 取值不存在时会报错

print(id_db.get(510824134010130534))  # 取值不报错,解决上面取值报错问题

dic2 = {
    'name': 'yes',
    220182143511229743: {  # Key必须唯一
        'name': "Da Xin Fan",
        'age': 28,
        'addr': 'FengDong'
    },
}
id_db.update(dic2)  # 更新值,id_db字典会和dic2字典同步
print(id_db)
print(id_db.items())  # 字典列表转换
print(id_db.values())  # 获取values
print(id_db.keys())  # 获取key值
print(220182143511229743 in id_db)  # 判断值是否在字典中
print(id_db.setdefault(220182143511229743, "N/A"))  # 取一个key如果存在就返回,如果不存在就添加默认值
print(id_db)

print(dict.fromkeys([1, 2, 3, 4, 5, 6, 7], "dddd"))  # 一个key对应一个value,生成新的字典

print(id_db.popitem())  # 随机删除

# 循环字典
for key in id_db:  # 效率比较高,推荐使用
    print(key, id_db[key])

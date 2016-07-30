#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# import memcache
#
# mc = memcache.Client(['172.16.131.129:12000', '172.16.131.128:12001', ], debug=True)
#
# mc.set("foo", "bar")
# ret = mc.get("foo")
# print(ret)

# debug = True 表示运行出现错误时，现实错误信息，上线后移除该参数。


# import memcache
#
# mc = memcache.Client(['123.126.105.34:10319'], debug=True)
# # mc.add('name', 'chenliang')
# # mc.add('name', 'chenliang')
# mc.get('name')

import memcache

mc = memcache.Client(['123.126.105.34:10319'], debug=True)
# 如果memcache中存在rename,则替换成功,否则异常
mc.replace('rename', 'chenliang')

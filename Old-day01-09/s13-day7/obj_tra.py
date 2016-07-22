#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import sqlite3


class SQLHelper:
    def fetch(self, sql):
        # print(self.hhost)
        # print(self.uusername)
        # print(self.pwd)
        print(sql)

    def create(self, sql):
        pass

    def remove(self, sql):
        pass

    def modify(self, sql):
        pass


obj = SQLHelper()
obj.hhost = "s1.salt.com"
obj.uusername = "chenliang"
obj.pwd = "123"
obj.fetch("select * from A")


obj2 = SQLHelper()
obj2.hhost = "s2.salt.com"
obj2.uusername = "chenliang"
obj2.pwd = "123456"
obj2.fetch("select * from A")
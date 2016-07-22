#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

from backend.commons import Foo


class MyFoo(Foo):
    def f1(self):
        print("before")
        super(MyFoo, self).f1()
        print("after")
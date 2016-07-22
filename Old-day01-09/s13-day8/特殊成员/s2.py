#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


class Foo:

    def __iter__(self):
        # return iter([11, 22, 33, 44, 55])
        yield 1
        yield 2
        yield 3

obj = Foo()
for item in obj:
    print(item)

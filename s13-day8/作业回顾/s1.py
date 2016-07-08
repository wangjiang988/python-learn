#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


class Foo:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


import pickle

obj = Foo('alex')

pickle.dump(obj, open('db', 'wb'))
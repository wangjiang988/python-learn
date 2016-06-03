#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang


def f1():
    print(123)


def f1():
    print(456)

f1()


def f1():
    print('123')


def f2(xxx):
    xxx()

f2(f1)
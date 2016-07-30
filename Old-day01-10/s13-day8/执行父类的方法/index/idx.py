#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang
from settings import ClassName
from settings import Path


def execute():
    model = __import__(Path, fromlist=True)
    cls = getattr(model, ClassName)
    obj = cls()
    obj.f1()
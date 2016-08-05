#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lang

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from conf import conf

engine = create_engine(conf.DB)
SessionCls = sessionmaker(bind=engine)
session = SessionCls()

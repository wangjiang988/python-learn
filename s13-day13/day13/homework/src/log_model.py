#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lang

from src import hm_schema
from src import db_conn
import datetime


def insert_log(user, hostuser, cmd_type, msg):
    log = hm_schema.AuditLog(userprofile_id=user.id, hostuser_id=hostuser.id, cmd_type=cmd_type, cmd=msg,
                            datetime=datetime.datetime.now())
    db_conn.session.add(log)
    db_conn.session.commit()

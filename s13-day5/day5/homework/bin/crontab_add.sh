#!/usr/bin/env bash

GPATH = `pwd`
MPATH = `cd ${GPATH}/../src ; pwd`

# 添加计划任务
echo "0 0 * * * python3 ${MPATH}/atm_crontab.py > /dev/null 2>&1" >> /var/spool/cron/root
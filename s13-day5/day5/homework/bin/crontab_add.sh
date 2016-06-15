#!/usr/bin/env bash

FWDIR="$(cd `dirname "${BASH_SOURCE-$0}"`; pwd)"

MPATH = `cd ${FWDIR}/../src ; pwd`

# 添加计划任务
echo "0 0 * * * python3 ${MPATH}/atm_crontab.py > /dev/null 2>&1" >> /var/spool/cron/root

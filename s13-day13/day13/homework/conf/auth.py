#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lang

from src import cmd_def

"""
认证配置，所有通过命令行参数调用的方法需要现在此认证方可调用
"""


actions = {
    'start': cmd_def.start,
    'init_database': cmd_def.init_database,
    'import_hosts': cmd_def.import_hosts,
    'import_remoteusers': cmd_def.import_remoteusers,
    'import_groups': cmd_def.import_groups,
    'import_users': cmd_def.import_users,
}

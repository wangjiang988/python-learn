#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 执行系统命令
import os

os.system("ls -al")
os.mkdir("pwd")
read = os.popen("df -hT").read()


# 查看系统路径
import sys
print(sys.path)

# 命令行下tab补全命令
# For MAC：
import sys
import readline
import rlcompleter

if sys.platform == 'darwin' and sys.version_info[0] == 2:
    readline.parse_and_bind("tab: complete")  # linux and python3 on mac
else:
    readline.parse_and_bind("bind ^I rl_complete")

# 说明：上面的代码如果在Mac上不好用，可以尝试下面的代码
# https://docs.python.org/2/library/rlcompleter.html
try:
    import readline
except ImportError:
    print("Module readline not available.")
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")


# For Linux:
#!/usr/bin/env python 
# python startup file 
import sys
import readline
import rlcompleter
import atexit
import os
# tab completion 
readline.parse_and_bind('tab: complete')
# history file 
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file, histfile)
del os, histfile, readline, rlcompleter


# 需要注意: 自己定义的模块都放到/usr/lib/python2.7/site-packages/
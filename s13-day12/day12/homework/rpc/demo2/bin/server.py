#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lang

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import rpc_server

if __name__ == '__main__':
    server = rpc_server.rpcServer()
    server.run()
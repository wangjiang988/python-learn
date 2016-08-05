#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lang

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from core import rpc_client

if __name__ == '__main__':
    client = rpc_client.rpcClient()
    if len(sys.argv) == 1:
        sys.stderr.write("Usage: %s [command]\n" % sys.argv[0])
    else:
        client.call(' '.join(sys.argv[1:]))
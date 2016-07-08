#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.client import ftp_client

if __name__ == '__main__':
    myclient = ftp_client()
    myclient.start()
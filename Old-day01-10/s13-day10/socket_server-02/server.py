#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import socketserver


class MyClass(socketserver.BaseRequestHandler):
    def handle(self):
        pass


if __name__ == '__main__':
    obj = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyClass)
    obj.serve_forever()
    obj.serve_forever()
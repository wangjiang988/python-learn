#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import socketserver
import subprocess


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.', encoding='utf8'))
        while True:
            try:
                data = self.request.recv(1024)
                if len(data) == 0:
                    break
                print("[%s] says: %s" % (self.client_address, data.decode()))
                cmd = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                cmd_res = cmd.stdout.read()
                if not cmd_res:  # 判断如果cmd_res不为空
                    cmd_res = cmd.stderr.read()
                if len(cmd_res) == 0:  # cmd has not output
                    cmd_res = bytes("cmd has output", encoding='utf8')
                self.request.send(cmd_res)
            except Exception:
                break

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8005), MyServer)
    server.serve_forever()

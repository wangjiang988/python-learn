#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

import socketserver
import subprocess
import json


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.', encoding='utf8'))
        while True:
            try:
                data = self.request.recv(1024)
                if len(data) == 0:
                    break
                print("[%s] says: %s" % (self.client_address, data.decode()))
                task_data = json.loads(data.decode())
                task_action = task_data.get("action")
                if hasattr(self, "task_%s" % task_action):
                    func = getattr(self, "task_%s" % task_action)
                    func(task_data)
                else:
                    print("task action is not supported", task_data)
            except Exception:
                break

    def task_put(self, *args, **kwargs):
        print("put", args, kwargs)
        filesize = args[0].get('file_size')
        filename = args[0].get('filename')
        server_response = {"status": 200}
        self.request.send(bytes(json.dumps(server_response), encoding='utf8'))
        f = open(filename, 'wb')
        recv_size = 0
        while recv_size < filesize:
            data = self.request.recv(4096)
            f.write(data)
            recv_size += len(data)
            print('filesize: %s  recvsize:%s' % (filesize, recv_size))
        print("file recv success")
        f.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8005), MyServer)
    server.serve_forever()

#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lazar


import paramiko
import cmd


class RunCommand(cmd.Cmd):
    """add_host
    Simple shell to run a command on the host """

    prompt = 'ssh > '

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.hosts = []
        self.connections = []

    def do_add_host(self, args):
        """Add the host to the host list"""
        if args:
            self.hosts.append(args.split(','))
        else:
            print("usage: host ")

    def do_connect(self, args):
        """run
        Connect to all hosts in the hosts list"""

        for host in self.hosts:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(
                paramiko.AutoAddPolicy())
            client.connect(host[0],
                           username=host[1],
                           password=host[2])
            self.connections.append(client)

    def do_run(self, command):
        """Execute this command on all hosts in the list"""
        if command:
            for host, conn in zip(self.hosts, self.connections):
                stdin, stdout, stderr = conn.exec_command(command)
                stdin.close()
                for line in stdout.read().splitlines():
                    print('host: %s: %s' % (host[0], line))
        else:
            print("usage: run ")

    def do_close(self, args):
        for conn in self.connections:
            conn.close()


if __name__ == '__main__':
    RunCommand().cmdloop()

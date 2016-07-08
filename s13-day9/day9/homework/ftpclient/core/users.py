#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

from conf import conf
import json
class user(object):
    def __init__(self, username, password, quota):
        self.__username = username
        self.__password = password
        self.__quota = quota

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_quota(self):
        return self.__quota


class users(object):
    def __init__(self):
        self.__users_file = conf.USERS_FILE
        self.__users = self.__read_users()


    def __read_users(self):
        """
        读取所有用户信息
        :return: 返回所有用户信息列表，失败则返回None
        """
        import codecs
        try:
            with codecs.open(self.__users_file, 'r', 'utf-8') as f:
                users = json.load(f)
            return users
        except Exception:
            return []

    def get_users(self):
        return self.__users

    def get_user(self, username):
        for user in self.__users:
            if user['username'] == username:
                res_user = user(user['username'], user['password'], user['quota'])
                return res_user
        else:
            return None
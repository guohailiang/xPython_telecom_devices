#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午12:13
# @Author  : zhuhao
# @Project : helloPython
# @File    : router_info.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 设备相关信息

import os
import xRouter.ip_utils as utils


class RouterInfo:
    __slots__ = ['_ip', '_user', '_password']

    def __init__(self, ip, user, password):
        self._ip = ip
        self._user = user
        self._password = password

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, new_ip):
        self._ip = new_ip

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, new_user):
        return self._user

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_passwd):
        self._password = new_passwd


def get_routers(file_path):
    """
    从文件中获取设备信息
    :param file_path: 文件路径
    :return: 设备信息列表
    """
    if not os.path.exists(file_path):
        return None
    routers = []
    with open(file_path) as fp:
        for line in fp:
            line = line.strip(' ').rstrip('\n')
            line_info = line.split(',')
            if not utils.ip_check(line_info[0]):
                continue
            router = RouterInfo(line_info[0], line_info[1], line_info[2])
            routers.append(router)
    return routers


if __name__ == '__main__':

    routers = get_routers('ip.txt')
    for r in routers:
        print(r.ip, r.user, r.password)

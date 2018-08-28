#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午1:21
# @Author  : zhuhao
# @Project : helloPython
# @File    : ip_utils.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 工具类

import re
import socket
import subprocess


def ip_check(ip):
    """
    ipv4 地址合法性检测
    :param ip: 待检测的ip地址
    :return: 如果合法，返回True，不合法返回False
    """
    if ip is None or len(ip) == 0:
        return False
    pattern = '^(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))$'
    p = re.compile(pattern)
    m = p.match(ip)
    if m is None:
        return False
    return True


def port_scan(ip_addr, port):
    """
    端口扫描
    :param ip_addr: 待扫描的主机地址
    :param port: 端口
    :return: 打开则返回True，失败返回False
    """
    if not ip_check(ip_addr):
        print("{0} is not a correct ip address.".format(ip_addr))
        return
    s = socket.socket()
    print("attempting to connect to {0} on port {1}.".format(ip_addr, port))
    result = s.connect_ex((ip_addr, port))
    s.close()
    if result == 0:
        print("success to connect to {0} on port {1}.".format(ip_addr, port))
        return True
    else:
        print("failed to connect to {0} on port {1}.".format(ip_addr, port))
        return False


def ip_up_down(ip_addr):
    """
    检测IP是否可达
    :param ip_addr:ip地址
    :return: 可达则返回True，否则返回False
    """
    if not ip_check(ip_addr):
        print("{0} is not a correct ip address.".format(ip_addr))
        return
    command = 'ping -c 3 ' + ip_addr
    ret = subprocess.call(command, shell=True)
    if ret == 0:
        print('{0} is up.'.format(ip_addr))
        return True
    else:
        print('{0} is down.'.format(ip_addr))
        return False


if __name__ == '__main__':
    # port_scan('127.0.0.1', 22)
    # print(ip_check('129.4.20.250'))
    ip_up_down('127.0.0.2')

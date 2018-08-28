#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 下午10:21
# @Author  : zhuhao
# @Project : xPython
# @File    : sysinfo.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 获取系统信息

import platform
import socket

def get_machine():
    """计算机类型"""
    return platform.machine()

def get_architecture():
    """获取操作系统位数"""
    return platform.architecture()

def get_system():
    """获取操作系统类型"""
    return platform.system()

def get_computerName():
    """获取计算机名称"""
    return socket.gethostname()

def get_node():
    '''计算机的网络名称'''
    return platform.node()

def get_ipaddr():
    """获取设备IP"""
    return socket.gethostbyname(socket.gethostname())

if __name__=='__main__':
    machine=get_machine()
    print(machine)
    print(get_architecture())
    print(get_system())
    print(get_computerName())
    print(get_node())
    print(get_ipaddr())
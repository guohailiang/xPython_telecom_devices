#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 上午12:08
# @Author  : zhuhao
# @Project : xPython
# @File    : get_interface_ip.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc:获取设备接口ip

from telnet_util import TelnetUtil
import re

def get_interface_ip(ip,user,password):
    '''
    获取设备的接口ip
    :param ip: 设备登录地址
    :param user: 用户名
    :param password: 密码
    :return:
    '''
    t=TelnetUtil(ip,user,password)
    if t.login():
        print('login successfully.')
        result=t.exec_command('display ip interface brief')
        results=result.split('\r\n')
        pattern=re.compile('^Vlanif|^Loop|^Gigabit')
        for line in results:
            line=line.strip()
            if pattern.match(line):
                print(line)
    t.close()
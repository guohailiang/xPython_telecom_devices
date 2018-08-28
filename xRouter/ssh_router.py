#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 上午12:19
# @Author  : zhuhao
# @Project : xPython
# @File    : ssh_router.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc: 使用ssh协议登录设备执行相关命令

import paramiko

class SSH_Router(object):
    '''
    使用ssh协议操作设备
    '''
    def __init__(self,ip,user,password):
        self._ip=ip
        self._user=user
        self._password=password
        self._ssh_client=paramiko.SSHClient()

    def _get_transport(self):
        '''
        设备登录
        :return:
        '''
        _transport=paramiko.Transport((self._ip,22))
        try:
            _transport.connect(username=self._user,password=self._password)
        except paramiko.SSHException as ex:
            print(ex)
            _transport=None
        return _transport

    def run_command(self,command):
        '''
        执行命令
        :param command: 待执行的命令
        :return:
        '''
        _transport=self._get_transport()
        if _transport is None:
            return
        self._ssh_client._transport=_transport
        stdin,stdout,stderr=self._ssh_client.exec_command(command.encode('ascii'))
        result=stdout.read().decode('utf-8')
        _transport.close()
        return result

    def close(self):
        '''
        关闭连接
        :return:
        '''
        if self._ssh_client._transport:
            self._ssh_client._transport.close()
        self._ssh_client.close()

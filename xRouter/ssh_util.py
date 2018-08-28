#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 下午10:19
# @Author  : zhuhao
# @Project : helloPython
# @File    : ssh_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 使用paramiko封装ssh2

import paramiko


class SSH_Util:
    '''
    使用ssh协议登录linux设备进行操作
    '''
    def __init__(self, ip, user, passwd, port=22):
        self.ip = ip
        self.user = user
        self.password = passwd
        self.port = port

    def _get_connection(self, timeout=3):
        """
        获取连接
        :param timeout:超时时间
        :return: 连接成功返回SSHClient实例，失败则返回None
        """
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            conn.connect(self.ip, self.port, self.user, self.password, timeout=timeout)
        except:
            conn.close()
            conn = None
        return conn

    def exec_command(self, command, timeout=3):
        """
        执行命令，返回执行结果
        :param command: 命令
        :param timeout: 超时时间
        :return:
        """
        conn = self._get_connection(timeout=timeout)
        if conn is None:
            return
        stdin, stdout, stderr = conn.exec_command(command, timeout=timeout)
        result = stdout.readlines().decode('utf-8')
        conn.close()
        return result

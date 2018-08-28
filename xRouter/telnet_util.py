#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午5:18
# @Author  : zhuhao
# @Project : helloPython
# @File    : telnet_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: telnetlib封装工具类

import telnetlib
import datetime
import re


def get_config_name(post_prefix='.cfg'):
    """
    按照当前日期组合文件名
    :param post_prefix:文件保存后缀名
    :return:
    """
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    month = '0' + month if len(month) < 2 else month
    day = str(now.day)
    day = '0' + day if len(day) < 2 else day
    cfg_name = year + month + day + post_prefix
    return cfg_name


class TelnetUtil:

    def __init__(self, ip, username, password, port=23, timeout=3):
        """
        构造函数
        :param ip: 设备ip
        :param username: 用户名
        :param password: 密码
        :param port: 端口，默认23
        :param timeout: 超时10s
        """
        self._ip = ip
        self._user = username
        self._passwd = password
        try:
            self._tn = telnetlib.Telnet(host=ip, port=port, timeout=timeout)
        except:
            print('Telnet failed,please check the network reachable.')
            self._tn = None

    def login(self, user_prompt="Username:", passwd_prompt="Password:"):
        """
        设备登录
        :param user_prompt: 用户名提示符
        :param passwd_prompt: 密码提示符
        :return: 成功返回True，错误返回False
        """
        if self._tn is None:
            return False
        self._tn.read_until(user_prompt, timeout=1)
        self._tn.write(self._user.encode('ascii') + '\n')
        self._tn.read_until(passwd_prompt, timeout=1)
        self._tn.write(self._passwd.encode('ascii') + '\n')
        result = self._tn.read_until('>'.encode('ascii'), timeout=3)
        if '>' not in result:
            print('用户名或者密码错误!!!')
            return False
        return True

    def exec_ctrl_c(self):
        """
        执行ctrl+c中断执行
        :return:
        """
        self._tn.write('\x03'.encode('ascii'))

    def save(self, save_cfg=None):
        """
        保存配置文件
        :param save_cfg: 配置文件名称，默认为None
        :return: 保存成功返回True，否则返回False
        """
        if save_cfg is None:
            self._tn.write('save '.encode('ascii') + '\n')
        else:
            save_cfg = get_config_name()
            device_name = self.get_device_name()
            device_name = device_name.lstrip('<').rstrip('>')
            save_cfg = device_name + '_' + save_cfg
            command = 'save ' + save_cfg
            self._tn.write(command.encode('ascii') + '\n')
        if save_cfg is None:
            self._tn.read_until('N]', timeout=1)
        else:
            self._tn.read_until('N]:',timeout=1)
        self._tn.write('y'.encode('ascii') + '\n')
        output = self._tn.read_until('successfully.', timeout=1).decode('utf-8')
        if 'successfully' in output:
            return True
        else:
            return False

    def exec_command(self, command, finish_char='>', timeout=3):
        """
        执行命令并返回命令执行结果
        :param command: 待执行的命令
        :param finish_char: 结束字符，默认为>
        :param timeout: 超时时间，默认为3s
        :return:
        """
        self._tn.write('\n')
        self._tn.write(command.encode('ascii') + '\n')
        output = self._tn.read_until(finish_char.encode('ascii'), timeout=timeout).decode('utf-8')
        return output

    def get_device_name(self,finish_char='>'):
        """
        获取设备名称
        :return: 返回设备名称
        """
        self._tn.write('\n')
        output = self._tn.read_until(finish_char.encode('ascii'), timeout=1).decode('utf-8')
        pattern = '<.*>'
        r = re.compile(pattern)
        m = r.findall(output)
        return m[0]

    def close(self):
        """
        关闭
        :return:
        """
        if self._tn is None:
            self._tn.close()


if __name__ == '__main__':
    print(get_config_name())

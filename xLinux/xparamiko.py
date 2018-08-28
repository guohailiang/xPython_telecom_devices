#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 下午1:06
# @Author  : zhuhao
# @Project : helloPython
# @File    : xparamiko.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 远程执行linux命令，上传，下载配置文件等

import os
import threading
import paramiko

lock = threading.Lock()


class Host:
    __slots__ = ['host', 'user', 'password', 'port']

    def __init__(self, host, username, password, port=22):
        self.host = host
        self.user = username
        self.password = password
        self.port = port

    def __repr__(self):
        return self.host + ',' + self.user + ',' + self.password + ',' + self.port


def log(logstr, file_name='cmdLog.log'):
    """
    将日志写文件
    :param logstr:日志
    :param file_name: 文件名称
    :return:
    """
    lock.acquire()
    with open(file_name, mode='a+') as fp:
        fp.write(logstr)
        fp.write('\n')
        fp.flush()
    lock.release()


def check_remote_connect(host, username, password, port=22):
    """
    远程环境检测
    :param host: 主机ip
    :param username: 用户名
    :param password: 密码
    :param port: 端口
    :return:
    """
    log('connect host {0} test.'.format(host))
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(host, port, username, password)
        stdin, stdout, stderr = ssh_client.exec_command("echo test", timeout=3)
        result = stdout.read().strip()
        ssh_client.close()
        if result == "test":
            log('success to connect host {0}.'.format(host))
            return True
        log('fail to connect host {0}.'.format(host))
        return False
    except Exception as ex:
        log('fail to connect host {0}'.format(host))
        return False


def exec_command(host, username, password, command, port=22):
    """
    远程执行命令
    :param host: 远程主机ip
    :param username: 用户名
    :param password: 密码
    :param command: 待执行的命令
    :param port: 端口
    :return:
    """
    log('exec command at host {0}.'.format(host))
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(host, port, username, password)
        stdin, stdout, stderr = ssh_client.exec_command(command.encode('ascii'), timeout=3)
        result = stdout.read().strip().decode('utf-8')
        print(result)
        log(result)
        return result
    except Exception as ex:
        log('fail to exec command at host {0}.'.format(host))
    finally:
        ssh_client.close()


def get_transport(host, username, password, port=22):
    """
    获取transport实例
    :param host: 远程主机ip
    :param username: 用户名
    :param password: 密码
    :param port: 端口
    :return: 连接成功返回实例，失败返回None
    """
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=username, password=password)
        return transport
    except paramiko.SSHException as ex:
        print(ex)
        return None


def upload(host, username, password, port=22, from_file="", to_dir=""):
    """
    文件上传
    :param host: 远程主机ip
    :param username: 用户名
    :param password: 密码
    :param port: 端口
    :param from_file: 本地上传文件
    :param to_dir: 远程保存的文件
    :return:
    """
    transport = get_transport(host, username, password, port)
    if transport is None:
        return False
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(from_file, to_dir)
    transport.close()
    return True


def download(host, username, password, port=22, from_file="", to_dir=""):
    """
    文件下载
    :param host: 远程主机ip
    :param username: 用户名
    :param password: 密码
    :param port: 端口
    :param from_file: 远程待下载文件
    :param to_dir: 本地保存的文件
    :return:
    """
    transport = get_transport(host, username, password, port)
    if transport is None:
        return False
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(from_file, to_dir)
    transport.close()
    return True


def get_hosts(file_name='hosts.txt'):
    """
    获取主机列表
    :param file_name: 主机文件名
    :return:
    """
    if not os.path.exists(file_name):
        print('file not exists.')
        return
    hosts = []
    with open(file_name) as fp:
        for line in fp:
            host_info = line.strip('\n').split(',')
            host = Host(host_info[0], host_info[1], host_info[2], host_info[3])
            hosts.append(host)
    return hosts


def batch_exec_command(host_list, command):
    """
    多线程多主机命令执行
    :param host_list: 主机列表
    :param command: 待执行的命令
    :return:
    """
    hosts = get_hosts(host_list)
    for host in hosts:
        t = threading.Thread(target=exec_command, args=(host.host, host.user, host.password, command, host.port))
        t.start()
        t.join()


if __name__ == '__main__':
    # check_remote_connect('127.0.0.1', 'zhuhao', '891407')
    hosts = get_hosts()
    for h in hosts:
        print(h)

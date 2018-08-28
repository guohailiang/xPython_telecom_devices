#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 下午10:57
# @Author  : zhuhao
# @Project : helloPython
# @File    : ftp_util.py
# @Contact : hyzhuhao891407@163.com
# @Software : PyCharm
# @Desc: ftp帮助

import os
import ftplib
from datetime import datetime
from router_info import get_routers
from threading import Thread

def append(line):
    """
    将内容写入文件中
    :param line: 待写入的行
    :return:
    """
    with open('ftp_log.txt', mode='a+') as fp:
        fp.write(line + '\n')
        fp.flush()


class FTPUtil:
    """FTP工具类"""
    def __init__(self, host, username, password, timeout=3):
        self.host = host
        self.username = username
        self.password = password
        self.timeout = timeout

        try:
            self.ftp = ftplib.FTP(host, username, password, timeout=timeout)
        except:
            self.ftp = None
            print('ftp login failed')

    def dir(self, args='.cfg', func=append):
        """
        列出所有以.cfg格式结尾的配置文件，并写入到文件中
        :param args: 过滤条件，默认为cfg格式的文件
        :param func:
        :return:
        """
        self.ftp.dir(args, func)

    def list_dir(self, args='.cfg'):
        """
        列出所有以.cfg格式结尾的配置文件，并以列表形式返回
        :param args:过滤条件，默认为cfg格式的文件
        :return:
        """
        result = self.ftp.nlst(args)
        return result

    def download(self, local_path='.',cfg_date=None):
        '''
        下载指定日期的配置文件
        :param local_path: 下载后保存的目录
        :param cfg_date: 需要下载的配置文件日期
        :return:
        '''
        if cfg_date is None:
            today=datetime.today()
            str_today=today.strftime("%Y%m%d")
        else:
            str_today=cfg_date
        dirs = self.list_dir()
        cfg=[]
        for file_cfg in dirs:
            if file_cfg.find(str_today)>-1:
                cfg.append(file_cfg)
        if len(cfg)==0:
            print('无法下载到指定日期的配置文件')
            return False
        if len(cfg)==1:
            new_cfg=cfg[0]
        else:
            new_cfg=cfg.sort()[-1]
        path = os.path.join(os.path.dirname(os.path.abspath(local_path)), new_cfg)
        f = open(path, mode='wb')
        try:
            self.ftp.retrbinary('RETR ' + new_cfg, f.write)
            return True
        except ftplib.error_perm:
            os.unlink(new_cfg)
            return False
        finally:
            f.close()

    def quit(self):
        """
        退出
        :return:
        """
        if self.ftp is not None:
            self.ftp.quit()


def auto_download(router):
    '''
    自动下载设备配置文件
    :param router:
    :return:
    '''
    ftp=FTPUtil(host=router.ip,username=router.user,password=router.password)
    if ftp.download():
        print('finish download {0}.'.format(router.ip))
    ftp.quit()

if __name__=='__main__':
    routers=get_routers('ip.txt')
    threads=[]
    for r in routers:
        t=Thread(target=auto_download,args=(r,))
        threads.append(t)
    for t in threads:
        t.start()
        t.join()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 上午12:35
# @Author  : zhuhao
# @Project : xPython
# @File    : router_save.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc: 自动保存设备配置

from threading import Thread
from telnet_util import TelnetUtil
from router_info import get_routers
from datetime import datetime

def auto_save(router,save_as=False):
    t=TelnetUtil(router.ip,router.user,router.password)
    if t.login():
        if save_as:
            device=t.get_device_name()
            str_date=datetime.now().strftime('%Y%m%d%H%M%S')
            cfg_file=device+'_'+str_date+'.cfg'
            t.save(save_cfg=cfg_file)
        else:
            t.save()
        print('finish save {0}.'.format(router.ip))


if __name__=='__main__':
    routers=get_routers('ip.txt')
    threads=[]
    for r in routers:
        t=Thread(target=auto_save,args=(r,False,))
        threads.append(t)
    for t in threads:
        t.start()
        t.join()


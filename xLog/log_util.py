#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 下午10:24
# @Author  : zhuhao
# @Project : xPython
# @File    : log_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc:利用logging模块实现日志记录

import os
import sys
import logging


class LogUtil:
    __log = logging.getLogger('root')
    # 日志文件
    __logfile = os.path.join(os.getcwd(), sys.argv[0].split('/')[-1].split('.')[0] + '.log')
    # 日志记录格式
    __fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

    __handle1 = logging.FileHandler(__logfile)
    __handle1.setFormatter(__fmt)

    __handle2 = logging.StreamHandler(stream=sys.stdout)
    __handle2.setFormatter(__fmt)

    __log.addHandler(__handle1)
    __log.addHandler(__handle2)
    __log.setLevel(logging.INFO)

    @classmethod
    def info(cls, message):
        fn, lno, func = sys._getframe().f_back.f_code.co_filename, sys._getframe().f_back.f_lineno, sys._getframe().f_back.f_code.co_name
        message = "[{0} {1} {2}]".format(fn, lno, func) + ' ' + message
        cls.__log.info(message)

    @classmethod
    def exception(cls, message):
        cls.__log.exception(message)

    @classmethod
    def error(cls, message):
        cls.__log.error(message,exc_info=True)


def main():
    LogUtil.info('hello world!')
    LogUtil.exception('exception')
    LogUtil.error('error')


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 下午10:08
# @Author  : zhuhao
# @Project : xPython
# @File    : log_decorate.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 利用类装饰器实现日志记录功能

import os
from datetime import datetime
from functools import wraps

log_file = os.path.join(os.getcwd(), "test.log")


class Log:

    def __init__(self, logfile=log_file):
        self.logfile = logfile

    def write_log(self, *args, **kwargs):
        '''
        将操作记录写入到文件中
        :param args:
        :param kwargs:
        :return:
        '''
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_str = now + ' 操作人:[{0}]执行了[{1}]操作.'.format(*args)
        with open(self.logfile, mode='a') as fp:
            fp.write(log_str + '\n')

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.write_log(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper


@Log()
def func(name, age):
    print('姓名：{0},年龄：{1}.'.format(name, age))


if __name__ == '__main__':
    func('zhuhao', 28)

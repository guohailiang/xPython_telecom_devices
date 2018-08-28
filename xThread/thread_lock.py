#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 上午7:38
# @Author  : zhuhao
# @Project : xPython
# @File    : thread_lock.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc: 利用类装饰器实现线程锁

import threading
from functools import wraps


class ThreadLock(object):

    def __init__(self):
        self.lock = threading.Lock()

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.lock.acquire()
            func(*args, **kwargs)
            self.lock.release()

        return wrapper


total = 0


@ThreadLock()
def add():
    global total
    total += 1


if __name__ == '__main__':
    threads = []
    for i in range(10):
        t = threading.Thread(target=add)
        threads.append(t)

    for t in threads:
        t.start()
        t.join()
    print(total)

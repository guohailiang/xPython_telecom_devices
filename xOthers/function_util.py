#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 下午9:44
# @Author  : zhuhao
# @Project : xPython
# @File    : function_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc:装饰器实现计算时间

from functools import wraps
import time


# 装饰器限制函数调用次数
def call_limit(func):
    a = [0]

    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        a[0] += 1
        print('{0} have call {1} times'.format(func.__name__, a[0]))
        return ret

    return wrapper


@call_limit
def func(x):
    print(x)


# 利用装饰器实现计算函数调用时间
def timecost(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        cost = end - start
        print('{0} exec time cost is {1} seconds.'.format(func.__name__, cost))
        return ret

    return wrapper


# 利用类装饰器计算函数执行时间

class TimeCost:

    def __init__(self):
        pass

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            end = time.time()
            cost = end - start
            print('{0} exec time cost is {1} seconds.'.format(func.__name__, cost))
            return ret

        return wrapper


@TimeCost()
def cost():
    time.sleep(3)
    print('finished')


if __name__ == '__main__':
    # func(1)
    # func(2)
    cost()

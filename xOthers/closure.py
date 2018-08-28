#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 下午11:36
# @Author  : zhuhao
# @Project : xPython
# @File    : closure.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc: 闭包和装饰器

import time
from functools import wraps


# 1.函数式装饰器：装饰带参数的函数，但是装饰器不带参数
def get_time(func):
    """
    计算函数运行时间的装饰器
    :param func: 待装饰的函数
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        cost = end - start
        print("the function {0} execute need {1} seconds.".format(func.__name__, cost))

    return wrapper


@get_time
def add(num1, num2):
    time.sleep(3)
    print("num1+num2={0}".format(num1 + num2))


# 2.函数式装饰器：装饰带参数的函数，且装饰器带参数
def before():
    print('begin to execute the function.')

def after():
    print('finish to execute the function.')

def aop(before, after):
    def out_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            before()
            func(*args, **kwargs)
            after()
        return inner_wrapper
    return out_wrapper

@aop(before,after)
def sub(num1,num2):
    print('execute the function sub.')
    return num1-num2

#3.类装饰器：不带参数的装饰器,装饰带参数的函数
class decorator(object):
    def __init__(self,func):
        self.func=func

    def __call__(self, *args, **kwargs):
        self.func(*args,**kwargs)

@decorator
def multiply(num1,num2):
    print("num1*num2={0}".format(num1*num2))

#4.类装饰器：带参数的装饰器，装饰带参数的函数,实现AOP
class decorator2(object):
    def __init__(self,arg1,arg2):
        self.arg1=arg1
        self.arg2=arg2

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            self.arg1()
            func(*args,**kwargs)
            self.arg2()
        return wrapper

@decorator2(before,after)
def divide(num1,num2):
    print('execute the function divide.')
    return num1/num2


if __name__ == "__main__":
    # add(1, 2)
    # sub(3,1)
    # multiply(2,3)
    divide(12,2)

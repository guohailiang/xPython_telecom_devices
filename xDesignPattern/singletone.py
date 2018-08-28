#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 下午8:05
# @Author  : zhuhao
# @Project : xPython
# @File    : singletone.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc:单例设计模式

from functools import wraps


# 1.利用__new__实现
class SingleTone(object):
    # 类私有属性
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SingleTone, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


# 2.利用函数式装饰器装饰类
def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):  # 类构造函数参数
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class MyClass(object):
    def __init__(self, val):
        self.__val = val

    def getVal(self):
        return self.__val


if __name__ == '__main__':
    # s1 = SingleTone()
    # s2 = SingleTone()
    # print(s1 == s2)
    #
    # print(id(s1), id(s2))
    s1 = MyClass(1)
    s2 = MyClass(2)
    print(s1 == s2)
    print(s1.getVal(), s2.getVal())

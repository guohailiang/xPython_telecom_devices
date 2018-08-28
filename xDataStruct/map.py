#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 下午7:45
# @Author  : zhuhao
# @Project : xPython
# @File    : map.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc: map实现

class _MapEntry(object):

    __slots__ = ['key','value']

    def __init__(self,key,value):
        self.key=key
        self.value=value

class Map(object):

    def __init__(self):
        self._entryList=list()
        self._size=0

    def size(self):
        return self._size

    def contains(self,key):
        pass

    def add(self,key,value):
        pass

    def get(self,key):
        pass

    def set(self,key,value):
        pass

    def remove(self,key):
        pass

    def __iter__(self):
        pass

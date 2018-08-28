#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 下午11:30
# @Author  : zhuhao
# @Project : xPython
# @File    : fifoCache.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc:利用OrderedDict实现FIFO算法,OrderedDict是按照元素插入时间排序的,最近的则在最后

from collections import OrderedDict

class FIFOCache:

    def __init__(self,max_cache_size=10):
        self.cache=OrderedDict()
        self.max_size=max_cache_size

    def set(self,key,value):
        '''
        添加元素，
        1.判断是否已满，如果已满则先删除最先插入的元素
        2.判断key是否存在，如果存在则直接返回其值
        3.不存在则直接添加
        :param key:
        :param value:
        :return:
        '''
        if self.max_size<=len(self.cache):
            #缓存已满,删除最先插入的元素
            self.cache.popitem(last=False)
            self.cache[key]=value
        elif self.cache.has_key(key):
            self.cache[key]=value
        else:
            self.cache[key]=value

    def get(self,key):
        '''
        获取元素，存在则先删除，再添加并返回对应的value；否则返回None
        :param key:
        :return:
        '''
        if self.cache.has_key(key):
            value=self.cache[key]
            return value
        else:
            return None

if __name__=='__main__':
    cache=FIFOCache()
    cache.set(3,3)
    cache.set(2,2)
    cache.set(1,1)
    print(cache.cache)
    cache.get(3)
    print(cache.cache)
    print(cache.cache)
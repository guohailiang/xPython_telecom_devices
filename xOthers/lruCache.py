#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 下午11:10
# @Author  : zhuhao
# @Project : xPython
# @File    : lruCache.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc:利用OrderedDict实现LRU算法,OrderedDict是按照元素插入时间排序的,最近访问的则在最后


from collections import OrderedDict


class LRUCache:

    def __init__(self, max_cache_size=10):
        self.cache = OrderedDict()
        self.max_size = max_cache_size

    def set(self, key, value):
        '''
        添加元素，
        1.判断是否已满，如果已满则先删除最近没有访问的一个元素
        2.判断key是否存在，如果存在则先删除，再执行添加
        3.不存在则直接添加
        :param key:
        :param value:
        :return:
        '''
        if self.max_size <= len(self.cache):
            # 缓存已满,删除最近没有访问一个元素
            self.cache.popitem(last=False)
            self.cache[key] = value
        elif self.cache.has_key(key):
            self.cache.pop(key)
            self.cache[key] = value
        else:
            self.cache[key] = value

    def get(self, key):
        '''
        获取元素，存在则先删除，再添加并返回对应的value；否则返回None
        :param key:
        :return:
        '''
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return None


class LRU_Cache:
    '''
    利用list和dict实现LRUCache功能;
    利用list保存key，实现LRU，最近访问的元素，其key在list中的前面
    '''

    def __init__(self, max_cache_size=10):
        self.keys = []
        self.cache = {}
        self.max_size = max_cache_size

    def set(self, key, value):
        if self.max_size <= len(self.cache):
            # 缓存已满,删除最近没有访问一个元素
            self.cache.pop(self.keys[0])
            self.keys.pop(0)
            self.keys.insert(0, key)
            self.cache[key] = value
        elif key in self.keys:
            self.keys.remove(key)
            self.keys.insert(0, key)
            self.cache[key] = value
        else:
            self.keys.insert(0, key)
            self.cache[key] = value

    def get(self, key):
        if key in self.keys:
            value = self.cache[key]
            self.keys.remove(key)
            self.keys.insert(0, key)
            return value
        else:
            return None


if __name__ == '__main__':
    cache = LRU_Cache()
    cache.set(3, 3)
    cache.set(2, 2)
    cache.set(1, 1)
    print(cache.keys)
    cache.get(3)
    print(cache.keys)

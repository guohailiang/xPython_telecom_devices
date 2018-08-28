#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 下午7:45
# @Author  : zhuhao
# @Project : xPython
# @File    : hashtable.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc:哈希表的簡單實現

class HashTable(object):
    '''
    哈希表，内部使用_items存储数据，每个元素也是列表，元素列表中存储了具体的(key,value)元组
    '''

    def __init__(self, size=10):
        '''
        构造函數
        :param size:哈希表中槽的個數
        '''
        self._size = size
        self._items = [[] for i in range(self._size)]

    def __hash(self, key):
        '''
        哈希函數
        :param key:
        :return:
        '''
        return key % self._size

    def insert(self, key, value):
        '''
        添加元素，元組个数（key，value）
        :param key:
        :param value:
        :return:
        '''
        index = self.__hash(key)
        # 先查找，找到后先刪除再添加
        if self._items[index]:
            for item in self._items[index]:
                if item[0] == key:
                    self._items[index].remove(item)
                    break
        self._items[index].append((key, value))

    def get(self, key):
        '''
        获取元素
        :param key:
        :return: 找到返回元素的值，否則产生keyerror异常
        '''
        index = self.__hash(key)
        if self._items[index]:
            for item in self._items[index]:
                if item[0] == key:
                    return item[1]
        raise KeyError

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.get(key)


if __name__=='__main__':
    hash_t=HashTable()
    hash_t.insert(1,'zhuhao');
    hash_t.insert(2,'shasha');
    hash_t.insert(11,'chenchen');
    print(hash_t[11])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 下午11:39
# @Author  : zhuhao
# @Project : xPython
# @File    : array.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 数组

import ctypes


class Array(object):

    def __init__(self, size):
        assert size > 0, 'array size must be >0'
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def clear(self, value):
        '''
        设置数组元素中所有元素的值为value
        :param value:
        :return:
        '''
        for i in range(len(self._elements)):
            self._elements[i] = value

    def __len__(self):
        '''
        获取数组长度
        :return:
        '''
        return self._size

    def __setitem__(self, index, value):
        '''
        设置数组中指定索引的值
        :param index:
        :param value:
        :return:
        '''
        assert index >= 0 and index < len(self), 'out of range'
        self._elements[index] = value

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), 'out of range'
        return self._elements[index]

    def __iter__(self):
        return ArrayIterator(self._elements)


class ArrayIterator(object):
    '''
    数组迭代器
    '''
    def __init__(self, items):
        self._items = items
        self._idx = 0

    def __iter__(self):
        return self

    def next(self):
        if self._idx < len(self._items):
            val = self._items[self._idx]
            self._idx += 1
            return val
        else:
            raise StopIteration


if __name__=='__main__':
    arr=Array(10)
    for i in range(10):
        arr[i]=i
    for item in arr:
        print(item)
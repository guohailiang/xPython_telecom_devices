#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 下午11:37
# @Author  : zhuhao
# @Project : xPython
# @File    : queue.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 利用列表实现队列

class Queue(object):
    __slots__ = ['_items', '_size']

    def __init__(self):
        self._items = []
        self._size = 0

    def empty(self):
        '''
        判断队列是否为空
        :return:
        '''
        return self._size == 0

    def size(self):
        '''
        获取队列大小
        :return:
        '''
        return self._size

    def enqueue(self, data):
        '''
        入队
        :param data:
        :return:
        '''
        self._items.append(data)
        self._size += 1

    def dequeue(self):
        '''
        出队
        :return:
        '''
        if self.empty():
            return None
        old_value = self._items.pop(0)
        self._size -= 1
        return old_value


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    while not q.empty():
        print(q.dequeue())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 下午11:36
# @Author  : zhuhao
# @Project : xPython
# @File    : stack.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 利用列表实现栈

class Stack(object):
    __slots__ = ['_items', '_size']

    def __init__(self):
        self._items = []
        self._size = 0

    def empty(self):
        '''
        判断栈是否为空
        :return:
        '''
        return self._size == 0

    def peek(self):
        '''
        获取栈顶元素的值
        :return:
        '''
        if self.empty():
            return None
        return self._items[-1]

    def size(self):
        '''
        获取栈的大小
        :return:
        '''
        return self._size

    def push(self, data):
        '''
        入栈
        :param data:
        :return:
        '''
        self._items.append(data)
        self._size += 1

    def pop(self):
        '''
        出栈
        :return:
        '''
        if self.empty():
            return None
        old_value = self._items.pop(-1)
        self._size -= 1
        return old_value

    def clear(self):
        '''
        清空栈
        :return:
        '''
        del self._items[:]
        self._size = 0


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.clear()
    while not s.empty():
        print(s.pop())

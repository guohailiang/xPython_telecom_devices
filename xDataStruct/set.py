#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 下午7:45
# @Author  : zhuhao
# @Project : xPython
# @File    : set.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc: 利用列表实现集合set功能

class Set(object):
    '''
    利用list实现集合功能
    '''

    def __init__(self):
        self._items = list()
        self._size = 0

    def __len__(self):
        '''
        获取集合大小
        :return:
        '''
        return self._size

    def size(self):
        '''
        获取集合大小
        :return:
        '''
        return self._size

    def add(self, elem):
        '''
        添加元素
        :param elem:
        :return: 添加成功返回True，失败返回False
        '''
        if elem in self:
            return False
        self._items.append(elem)
        self._size += 1
        return True

    def remove(self, elem):
        '''
        删除元素
        :param elem: 待删除的元素
        :return: 删除成功返回True，失败返回False
        '''
        if elem in self:
            self._items.remove(elem)
            self._size -= 1
            return True
        return False

    def isSubsetOf(self, other_set):
        '''
        判断当前集合是否other_set的子集
        :param other_set:
        :return:
        '''
        if not isinstance(other_set, Set):
            return False
        if self.size() > other_set.size():
            return False
        flag = True
        for item in self:
            if item not in other_set:
                flag = False
                break
        return flag

    def union(self, other_set):
        '''
        求2个集合的并集
        :param other_set:
        :return:
        '''
        if not isinstance(other_set, Set):
            return None
        result = []
        result.extend(self)
        for item in other_set:
            if item not in result:
                result.append(item)
        return result

    def intersect(self, other_set):
        '''
        求2个集合的交集
        :param other_set:
        :return:
        '''
        if not isinstance(other_set, Set):
            return None
        result = []
        for item in self:
            if item in other_set:
                result.append(item)
        return result

    def difference(self, other_set):
        '''
        求2个集合的差集
        :param other_set:
        :return:
        '''
        if not isinstance(other_set, Set):
            return None
        result = []
        for item in self:
            if item not in other_set:
                result.append(item)
        return result

    def contains(self, item):
        '''
        判断集合是否包含元素
        :param item:
        :return: 包含返回True，否则返回False
        '''
        if item in self:
            return True
        return False

    def __iter__(self):
        return _SetIterator(self._items)

    def __eq__(self, other_set):
        '''
        判断2个集合是否相等
        :param other_set:
        :return:
        '''
        if not isinstance(other_set, Set):
            return False

        if self.size() != other_set.size():
            return False
        flag = True
        for item in self:
            if item not in other_set:
                flag = False
                break
        return flag


class _SetIterator(object):
    '''
    集合迭代器
    '''

    def __init__(self, seq):
        self._items = seq
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


if __name__ == '__main__':
    s1 = Set()
    s2 = Set()

    s1.add(1)
    s1.add(2)
    s1.add(3)

    s2.add(3)
    s2.add(4)
    s2.add(5)

    print(s1.union(s2))
    print(len(s1))
    print(s1.intersect(s2))
    print(s1.difference(s2))

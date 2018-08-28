#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 下午7:59
# @Author  : zhuhao
# @Project : xPython
# @File    : singleLinkList.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 单链表实现

class Node(object):
    '''
    单链表节点
    '''
    __slots__ = ['_data', '_next']

    def __init__(self, data, next):
        self._data = data
        self._next = next

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, newNext):
        self._next = newNext

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, newData):
        self._data = newData


class SingleLinkedList(object):
    '''
    单链表
    '''

    def __init__(self):
        self._head = None
        self._size = 0

    def prepend(self, value):
        '''
        在单链表头部添加节点
        :param value:
        :return:
        '''
        root = self._head
        node = Node(data=value, next=None)
        if root is None:
            self._head = node
        else:
            node.next = root
            self._head = node
        self._size += 1
        return True

    def append(self, value):
        '''
        在单链表尾部添加节点
        :param value:
        :return:
        '''
        root = self._head
        node = Node(value, None)
        while root.next is not None:
            root = root.next
        root.next = node
        self._size += 1
        return True

    def size(self):
        '''
         获取单链表的长度
        :return:
        '''
        return self._size

    def insert(self, index, value):
        '''
        在单链表指定位置添加元素，从1开始
        :param index:
        :param value:
        :return:
        '''
        if index <= 1:
            return self.prepend(value)
        if index >= self._size:
            return self.append(value)
        root = self._head
        # 寻找插入位置
        node = Node(value, None)
        k = 1
        while root is not None and k < index:
            root = root.next
            k += 1
        node.next = root.next
        root.next = node
        self._size += 1
        return True

    def delete(self, index):
        '''
        删除指定位置的元素，从1开始
        :param index:
        :return:成功返回删除前节点的值
        '''
        if self.empty():
            raise Exception('the list is empty,can not delete.')
        if index<1 or index>self._size:
            raise IndexError('index {0} is out of range.'.format(index))
        k=1
        root=self._head
        prev=None
        #root指向待删除的节点，prev为删除的前一个节点
        while root is not None and k<index:
            prev=root
            root=root.next
            k+=1
        data=root.data
        prev.next=root.next
        return data

    def empty(self):
        '''
        判断单链表是否为空
        :return:
        '''
        return self._head is None

    def getValue(self, index):
        '''
        获取指定位置的元素值,从1开始
        :param index:
        :return:
        '''
        if self.empty():
            return
        if index < 1 or index > self._size:
            raise IndexError('index {0} is out of range.'.format(index))
        root = self._head
        k = 1
        while root is not None and k < index:
            root = root.next
            k += 1
        return root.data

    def delValue(self, value):
        '''
        删除第一个值为value的元素节点
        :param index:
        :return:成功返回True，失败返回False
        '''
        if self.empty():
            return False
        root=self._head
        prev=None
        while root is not None and root.data!=value:
            prev=root
            root=root.next
        if root is None: #没有找到value的节点
            return False
        prev.next=root.next
        return True

    def reverse(self):
        '''
        将单链表逆置
        :return:
        '''
        if self.empty():
            return
        root=self._head
        newlist=SingleLinkedList()
        while root is not None:
            newlist.prepend(root.data)
            root=root.next
        return newlist

    def update(self, index, value):
        '''
        修改指定位置的元素值,从1开始
        :param index:
        :param value:
        :return:
        '''
        if self.empty():
            return False
        if index < 1 or index > self._size:
            raise IndexError('index {0} is out of range.'.format(index))
        root = self._head
        k = 1
        while root is not None and k < index:
            root = root.next
            k += 1
        root.data=value
        return True

    def show(self):
        '''
        单链表输出
        :return:
        '''
        print('-------------------------')
        root = self._head
        while root is not None:
            print root.data,
            root = root.next
        print('\n-------------------------')


if __name__ == '__main__':
    linkList = SingleLinkedList()
    linkList.prepend(1)
    linkList.prepend(2)
    linkList.append(3)
    linkList.show()
    # linkList.insert(2, 4)
    # linkList.show()
    # linkList.delete(3)
    # linkList.show()
    # linkList.update(3,10)
    # linkList.show()
    newList=linkList.reverse()
    newList.show()
    newList.delValue(2)
    newList.show()

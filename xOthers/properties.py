#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 下午10:44
# @Author  : zhuhao
# @Project : xPython
# @File    : properties.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc: 利用字典实现Java的properties

class Properties:

    def __init__(self):
        self._pros = {}

    def put(self, key, value):
        '''
        增加属性信息
        :param key:
        :param value:
        :return:
        '''
        if key is None or key.strip() == "":
            raise Exception("the key can not be null.")
        self._pros[key] = value

    def get(self, key):
        '''
        获取属性信息
        :param key:
        :return:
        '''
        if key is None or key.strip() == "":
            raise Exception("the key can not be null.")
        if key not in self._pros:
            raise Exception("the key is not exists.")
        return self._pros[key]

    def setPros(self, newPros):
        '''
        设置新属性
        :param newPros:
        :return:
        '''
        if newPros is not None and len(newPros) > 0:
            self._pros = newPros

    def getProps(self):
        '''
        获取所有属性信息
        :return:
        '''
        lines = []
        for key in self._pros:
            lines.append("{0}={1}".format(key, self.get(key)))
        return lines


def appendProperties(fname, prop):
    '''
    将属性信息追加到文件末尾
    :param fName:
    :param prop:
    :return:
    '''
    lines = prop.getProps()
    with open(fname, 'ab') as f:
        for line in lines:
            f.write(line.encode("utf-8"))
            f.write("\n")


def saveProperties(fname, prop):
    '''
    保存属性信息至文件中
    :param fname:
    :param prop:
    :return:
    '''
    lines = prop.getProps()
    with open(fname, 'w+') as f:
        for line in lines:
            f.write(line.encode("utf-8"))
            f.write("\n")


def loadProperties(fname):
    '''
    将文件中的键值对属性信息加载到对象中
    :param fname:
    :return:
    '''
    prop = Properties()
    with open(fname, 'r') as f:
        for line in f:
            if line.strip() == "":
                continue
            keyValue = line.split("=")
            if len(keyValue) == 2:
                prop.put(keyValue[0].strip(), keyValue[1].strip())
    return prop

if __name__=="__main__":
    # p=Properties()
    # p.put("name","zhuhao")
    # p.put("age",18)
    # saveProperties("prop.txt",p)
    p=loadProperties("prop.txt")
    print(p.getProps())
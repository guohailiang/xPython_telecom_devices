#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 下午10:52
# @Author  : zhuhao
# @Project : xPython
# @File    : codeLineCount.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 计算文件目录下指定后缀名称的文件行数计算

import os

filelist=[]
whitelist=['py','cpp']

def getFileLines(filename):
    '''
    计算文件的行数
    :param filename:
    :return:
    '''
    count=0
    for index,line in enumerate(open(filename)):
        count+=1
    return count

def getFile(dirname):
    '''
    遍历目录，获取指定格式的文件
    :param dirname:
    :return:
    '''
    global filelist,whitelist
    for root,dirs,files in os.walk(dirname):
        for file in files:
            filepath=os.path.join(root,file)
            ext=file.split('.')[-1]
            if ext in whitelist:
                line_num=getFileLines(filepath)
                filelist.append(filepath)
                print('{0}:{1}'.format(filepath,line_num))


if __name__=='__main__':
    getFile('/Users/zhuhao/Python/xPython')
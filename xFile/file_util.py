#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 下午11:04
# @Author  : zhuhao
# @Project : xPython
# @File    : file_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc:文件帮助类

import time
import os


def timeStampToTime(timestamp):
    '''
    把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12
    :param timestamp: 需要转换的时间，float型
    :return:
    '''
    time_struct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_struct)

def get_file_ext(filename):
    '''
    获取文件后缀
    :param filename:
    :return:
    '''
    filename=unicode(filename,'utf-8')
    return os.path.splitext(filename)[-1]

def get_fileSize(filename):
    '''
    获取文件大小
    :param file_path: 文件名
    :return: 文件大小，单位M
    '''
    if not os.path.exists(filename):
        raise Exception('file {0} not exists.'.format(filename))
    filename=unicode(filename,'utf-8')
    fsize=os.path.getsize(filename)
    fsize=fsize/float(1024*1024)
    return round(fsize,2)

def get_accessTime(filename):
    """获取文件的访问时间"""
    if not os.path.exists(filename):
        raise Exception('file {0} not exists.'.format(filename))
    filename=unicode(filename,'utf-8')
    access_time=os.path.getatime(filename)
    return timeStampToTime(access_time)

def get_createTime(filename):
    """获取文件的创建时间"""
    if not os.path.exists(filename):
        raise Exception('file {0} not exists.'.format(filename))
    filename=unicode(filename,'utf-8')
    create_time=os.path.getctime(filename)
    return timeStampToTime(create_time)

def get_modifyTime(filename):
    """获取文件的修改时间"""
    if not os.path.exists(filename):
        raise Exception('file {0} not exists.'.format(filename))
    filename=unicode(filename,'utf-8')
    modify_time=os.path.getmtime(filename)
    return timeStampToTime(modify_time)

def getFilesByExt(dir,ext):
    """
    获取指定文件夹下指定格式的文件
    :param dir:
    :param ext:
    :return:
    """
    if not os.path.isdir(dir):
        print('{0} is not a directory.'.format(dir))
        return None
    if not os.path.exists(dir):
        print('{0} is not exists.'.format(dir))
        return None
    result=[]
    for root,dir,files in os.walk(dir):
        for file in files:
            filepath=os.path.join(root,file)
            file_ext=os.path.splitext(filepath)[1]
            if file_ext==ext:
                result.append(filepath)
    return result

def getDirSize(dir):
    """
    获取文件夹大小
    :param dir:
    :return:
    """
    size=0L
    for root,dirs,files in os.walk(dir):
        for file in files:
            size+=os.path.getsize(os.path.join(root,file))
            print(os.path.join(root,file))
    return size/(1024*1024)

if __name__=='__main__':
    # print(timeStampToTime(1479264792))
    # print(get_fileSize('/Users/zhuhao/Downloads/hwc2.0.20180213.part1.rar'))
    # print(get_accessTime('/Users/zhuhao/Shell/test1.sh'))
    # print(get_createTime('/Users/zhuhao/Shell/test1.sh'))
    # print(get_modifyTime('/Users/zhuhao/Shell/test1.sh'))
    # size=getDirSize('/Users/zhuhao/Python/xPython/')
    # print(str(size)+'M')
    print(getFilesByExt('/Users/zhuhao/Python/xPython/','.xlsx'))
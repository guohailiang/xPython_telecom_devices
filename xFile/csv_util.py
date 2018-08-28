#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 上午8:00
# @Author  : zhuhao
# @Project : xPython
# @File    : csv_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: csv文件帮助类

import os
import csv
import file_util


def list_to_csv(filename, datas=[]):
    '''
    将一个列表写入到csv文件中
    :param filename: 文件名
    :param datas: 需要写入的列表数据
    :return: 成功返回True，格式不对，抛出异常
    '''
    ext = file_util.get_file_ext(filename)
    if not ext in ['.csv']:
        raise Exception('file extension should be csv formatter.')
    with open(filename, 'w') as fp:
        csv_writer = csv.writer(fp)
        for row in datas:
            csv_writer.writerow(row)
    return True


def csv_to_list(filename):
    '''
    将文件中的数据读取到列表中
    :param filename: 文件名
    :return:
    '''
    if not os.path.exists(filename):
        raise Exception('file {0} is not exixts.'.format(filename))
    ext = file_util.get_file_ext(filename)
    if not ext in ['.csv', '.txt']:
        raise Exception('file extension should be csv formatter.')
    datas = []
    with open(filename) as fp:
        csv_reader = csv.reader(fp)
        for line in csv_reader:
            datas.append(line)
    return datas

def csv_to_dict(csv_file,fieldnames=None):
    '''
    将csv文件中的数据读入成dict类型
    :param csv_file:csv格式文件
    :param fieldnames:表头列名
    :return:
    '''
    if not os.path.exists(csv_file):
        raise Exception('file {0} is not exixts.'.format(csv_file))
    ext = file_util.get_file_ext(csv_file)
    if not ext in ['.csv']:
        raise Exception('file extension should be csv formatter.')
    fields=len(fieldnames)
    if fields<=0:
        raise Exception('the fieldnames can not be empty.')
    with open(csv_file) as fp:
        reader=csv.DictReader(fp,fieldnames)
        for row in reader:
            for i in range(len(fieldnames)):
                print row[fieldnames[i]] ,
            print('')

def dict_to_csv(csv_file,fieldnames,dict_data):
    '''
    将字典数据写入到csv文件中
    :param csv_file:csv格式文件
    :param fieldnames:表头列名
    :param dict_data:字典数据
    :return:
    '''
    ext = file_util.get_file_ext(csv_file)
    if not ext in ['.csv']:
        raise Exception('file extension should be csv formatter.')
    with open(csv_file, 'w') as fp:
        writer=csv.DictWriter(fp,fieldnames)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
    return True

csv_columns = ['Row','Name','Country']
dict_data = [
    {'Row': 1, 'Name': 'Alex', 'Country': 'India'},
    {'Row': 2, 'Name': 'Ben', 'Country': 'USA'},
    {'Row': 3, 'Name': 'Shri Ram', 'Country': 'India'},
    {'Row': 4, 'Name': 'Smith', 'Country': 'USA'},
    {'Row': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
    ]

if __name__ == '__main__':
    # datas=[['1','2',3],[4,5,6],['7',8,9]]
    # list_to_csv('datas.csv',datas)
    # datas=csv_to_list('datas.csv')
    # print(datas)
    # dict_to_csv('dict_data.csv',csv_columns,dict_data)
    csv_to_dict('dict_data.csv',csv_columns)

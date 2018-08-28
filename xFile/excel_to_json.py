#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 下午8:46
# @Author  : zhuhao
# @Project : xPython
# @File    : excel_to_json.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc: 将excel转换为json格式文件

import os
import json
from excel_util import ExcelHelper
from file_util import getFilesByExt
from threading import Thread


class ExcelToJson(object):

    def __init__(self,filePath,columns=[]):
        self._filepath=filePath
        self._header=columns
        self.checkFile(filePath)

    def checkFile(self,filePath):
        """
        检测文件路径是否存在，文件格式是否为excel2007格式
        :return:
        """
        if filePath is None or len(filePath)==0:
            raise Exception('filePath:{0} should not be empty.'.format(filePath))
        if not os.path.exists(filePath):
            raise Exception('the file path {0} is not exists.'.format(filePath))
        if not os.path.isfile(filePath):
            raise Exception('the file path {0} is not a file.'.format(filePath))
        ext=os.path.splitext(filePath)[1]
        if not ext=='.xlsx':
            raise Exception('the file {0} is not a excel file.'.format(filePath))
        return True

    def toJson(self):
        """
        将excel中的内容转换为json格式的数据
        :return:
        """
        excel=ExcelHelper(self._filepath)
        rows=excel.get_rownum()
        cols=len(self._header)
        result=[]
        for i in range(1,rows+1):
            row=dict()
            for j in range(1,cols+1):
                row[self._header[j-1]]=excel.get_cell_value(i,j)
            result.append(row)
        print(json.dumps(result))

def thread_to_json(dir):
    """
    多线程将dir下面的.xlsx文件转换为json
    :param dir:
    :return:
    """
    files=getFilesByExt(dir,'.xlsx')
    nums=len(files)
    if files is None or nums==0:
        return
    for i in range(nums):
        ins=ExcelToJson(files[i],['name','age','sex'])
        t=Thread(target=ins.toJson)
        t.start()
        t.join()


if __name__=='__main__':
    # try:
    #     ins=ExcelToJson('json.xlsx',['name','age','sex'])
    #     ins.toJson()
    # except Exception as ex:
    #     print(ex)
    # ins=ExcelToJson('json.xlsx',['name','age','sex'])
    # result=ins.toJson()
    # print(result)
    thread_to_json('/Users/zhuhao/Python/xPython/')
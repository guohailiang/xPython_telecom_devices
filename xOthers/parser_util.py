#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 下午8:50
# @Author  : zhuhao
# @Project : xPython
# @File    : parser_util.py
# @Contact : hyzhuhao891407@163.com
# @Software : PyCharm
# @Desc: 解析参数方法库optionParse的使用
# Python 有两个内建的模块用于处理命令行参数：
# 1.是 getopt，只能简单处理 命令行参数；
# 2.另一个是 optparse，它功能强大，而且易于使用。

from optparse import OptionParser

def main():
    '''add_option参数类型：
    action是有store(默认)，store_true，store_false等，
    dest是存储的变量，
    type是类型
    default是缺省值，
    help是帮助提示'''
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)

    parser.add_option("-f", "--file", dest="filename",
                      help="read data from FILENAME")
    # 当解析到 ‘-v’，options.verbose 将被赋予 True 值，反之，解析到 ‘-q’，会被赋予 False 值。
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    if options.verbose:
        print("reading %s..." % options.filename)


if __name__ == '__main__':
    """示例:python parser_util.py -f a.txt 123
    options为{'verbose': True, 'filename': 'a.txt'}，
    args为['123']"""
    main()

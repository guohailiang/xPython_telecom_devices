#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 上午11:54
# @Author  : zhuhao
# @Project : xPython
# @File    : yaml_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 操作yaml文件

import os


try:
    import yaml
except ImportError as ex:
    raise Exception(ex)


class YamlUtil:
    """yaml文件操作"""

    @staticmethod
    def load(filename):
        if not os.path.exists(filename):
            print("{0} is not exists.".format(filename))
            return
        with open(filename) as fp:
            result = yaml.load(fp)
        return result

    @staticmethod
    def dump_to_file(data, filename):
        """将数据序列化成yaml格式文件中"""
        if not os.path.exists(filename):
            print("{0} is not exists.".format(filename))
            return False
        with open(filename, mode='w') as fp:
            yaml.dump(data, fp)
        return True

    @staticmethod
    def dump_to_str(data):
        """将数据序列化成yaml格式字符串"""
        return yaml.dump(data)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('zhangsan', 19)
p2 = Person('lisi', 20)
p3 = Person('wangwu', 21)

persons = [p1, p2, p3]

if __name__ == '__main__':
    filename = os.path.join(os.getcwd(), 'cfg.yaml')
    cfg_yaml = YamlUtil.load(filename)
    print(cfg_yaml)
    if 'children' in cfg_yaml:
        print(cfg_yaml['children'])

    # print(YamlUtil.dump_to_str(persons))

    cfg_yaml['age']=10
    YamlUtil.dump_to_file(cfg_yaml,filename)

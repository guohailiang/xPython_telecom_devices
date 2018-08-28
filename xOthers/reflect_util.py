#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 下午4:55
# @Author  : zhuhao
# @Project : xPython
# @File    : reflect_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc:反射帮助类

'''
Python 2.x中默认都是经典类，只有显式继承了object才是新式类;Python 3.x中默认都是新式类,经典类被移除，不必显式的继承object
'''

import inspect


class Cat(object):
    __slots__ = ('name')

    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("hello,{1}.".format(self.name))


class ReflectUtil(object):

    @staticmethod
    def get(obj, attr):
        '''
        获取对象的属性值
        :param obj: 对象
        :param attr: 属性名称
        :return:
        '''
        if hasattr(obj, attr):
            return getattr(obj, attr)
        else:
            return None

    @staticmethod
    def set(obj, attr, value):
        '''
        设置对象的属性对应的值
        :param obj:
        :param attr:
        :param value:
        :return:
        '''
        if hasattr(obj, '__slots__'):
            if hasattr(obj, attr):
                setattr(obj, attr, value)
            else:
                print('can not set the attr for the obj,because it has the __slots__ config.')
        else:
            setattr(obj, attr, value)

    @staticmethod
    def create_instance(module_name, class_name, *args, **kwargs):
        '''
        创建对象实例
        :param module_name: 类所在模块
        :param class_name: 类名
        :param args: 构造函数参数
        :param kwargs: 构造函数参数
        :return: 返回对象实例
        '''
        try:
            module = __import__(module_name)  # 动态加载模块
            # obj=globals()[class_name](*args,**kwargs)
            obj = getattr(module, class_name)(*args, **kwargs)
            return obj
        except ImportError as ex:
            return None
        except AttributeError as ex:
            return None

    @staticmethod
    def getfuncbymodule(module_name, func_name):
        '''
        根据模块名和函数名获取其函数对象
        :param module_name: 模块名称
        :param func_name: 函数名称
        :return:
        '''
        try:
            module = __import__(module_name)
            return getattr(module, func_name)
        except ImportError as ex:
            return None
        except AttributeError as ex:
            return None


if __name__ == '__main__':
    cat = Cat('cat')
    # ReflectUtil.set(cat, 'age', 1)
    print(ReflectUtil.get(cat, 'name'))
    cat1 = ReflectUtil.create_instance('reflect_util', 'Cat1', 'cat2')
    print(cat1)

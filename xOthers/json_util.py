#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 下午8:14
# @Author  : zhuhao
# @Project : xPython
# @File    : json_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc: json与object对象之间互转

import json

class Person(object):

    def __init__(self,name,age):
        self.name=name
        self.age=age

def object_to_json(obj):
    '''
    将obj转换为json
    :param obj: obj对象
    :return: json格式的obj
    '''
    result={}
    result['__class__']=obj.__class__
    result['__module__']=obj.__module__
    #直接添加对象属性到result字典中
    result.update(obj.__dict__)
    return result

def json_to_object(dict_obj):
    '''
    将json转为对象object
    :param dict_obj: 
    :return: 
    '''
    result=dict(dict_obj)
    if '__class__' in dict_obj:
        class_name=dict_obj.pop('__class__')
        module_name=dict_obj.pop('__module__')
        module=__import__(module_name)
        obj_class=getattr(module,class_name)
        kwargs=dict((key.encode('ascii'), value) for key, value in dict_obj.items())
        obj=obj_class(**kwargs)
        return obj
    else:
        return result

if __name__=='__main__':
    p=json_to_object({'age': 28, '__module__': 'json_util', '__class__': 'Person', 'name': 'zhuhao'})
    print(p.name)
    print(p.age)

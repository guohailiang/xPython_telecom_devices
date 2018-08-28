#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 下午11:32
# @Author  : zhuhao
# @Project : xPython
# @File    : runaction.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc:利用反射实现类中的方法调用

import os
import sys
import types

MODULE_ROOT=os.path.join(os.path.dirname(__file__),"xDataStruct")

sys.path.append(MODULE_ROOT)

class RunAction:

    def __init__(self):
        self._plugins=self._load()

    def _load(self):
        '''
        加载模块中所有的类并保存到字典中
        :return:
        '''
        plugins={}
        print("load all class from {0}".format(MODULE_ROOT))
        for item in os.listdir(MODULE_ROOT):
            fn=str(item)
            if not fn.endswith(('.py','.pyc')):
                continue
            modulestr=fn[:-3]
            try:
                module=__import__(modulestr)
            except:
                print("{0} load exception.".format(MODULE_ROOT))
                continue
            for name in dir(module):
                obj=getattr(module,name)
                if obj and isinstance(obj,(type,types.ClassType)):
                    plugins[name]=obj
        return plugins

    def runAction(self,classname,methodname,*args):
        '''
        利用反射执行类中的方法
        :param classname:类名
        :param methodname:方法名
        :param args:构造函数参数
        :return:
        '''
        if not self._plugins.has_key(classname):
            print("does not find the classname({0}).".format(classname))
            return 1
        classobj=self._plugins[classname]
        method=getattr(classobj,methodname)
        try:
            if method and getattr(method,'__call__'):
                #调用类中构造函数创建对象
                classins=classobj(*args)
                #调用类中的方法
                return method(classins)
            else:
                print("does not find the classname({0}.{1}).".format(classname,methodname))
        except:
            print("")
            return 1

if __name__=='__main__':
    run_action=RunAction()
    result=run_action.runAction("Hello","say",'zhangsan')



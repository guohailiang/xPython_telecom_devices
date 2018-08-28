#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 上午8:35
# @Author  : zhuhao
# @Project : xPython
# @File    : config_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 读写ini格式的配置文件

import os
import ConfigParser


class ConfigUtil:

    def __init__(self, filename):
        filename = unicode(filename, 'utf-8')
        if os.path.exists(filename):
            self._file = filename
            self._cfg = ConfigParser.ConfigParser()
            self._cfg.read(filename)

    def _is_exists(self, section, key):
        """判断key是否存在"""
        return self._cfg.has_option(section, key)

    def _is_section_exists(self,section):
        """判断section是否存在"""
        return self._cfg.has_section(section)

    def get(self, section, key):
        """获取section下对应key的值"""
        if not self._is_exists(section, key):
            print('{0} is not exists.'.format(key))
            return
        result = self._cfg.get(section, key)
        return result

    def set(self, section, key, value):
        """设置section下对应key的值"""
        if not self._is_section_exists(section):
            self._cfg.add_section(section)
        try:
            self._cfg.set(section, key, value)
            self._cfg.write(open(self._file, mode='w'))
            return True
        except Exception as ex:
            print(ex)
            return False

    def remove(self,section,key):
        """删除section下对应key的值"""
        if not self._is_exists(section,key):
            print('{0} is not exists.'.format(key))
            return False
        self._cfg.remove_option(section,key)
        self._cfg.write(open(self._file, mode='w'))
        return True

if __name__=='__main__':
    file_path=os.path.join(os.getcwd(),"config.cfg")
    cfg_util=ConfigUtil(file_path)
    print(cfg_util.get('test','logpath'))
    cfg_util.set('linux','name','mac')
    print(cfg_util.get('linux','name'))
    cfg_util.remove('linux','name')
    print(cfg_util.get('linux', 'name'))

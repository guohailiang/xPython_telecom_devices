#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 下午7:07
# @Author  : zhuhao
# @Project : xPython
# @File    : mongoUtil.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc:mongodb操作封装类

try:
    from pymongo import MongoClient
except ImportError as error:
    raise Exception(error)


class MongoUtil:
    """MongoDB封装"""

    def __init__(self, host='localhost', port=27017, database_name=None, collection_name=None):
        try:
            self._connection = MongoClient(host=host, port=port, connectTimeoutMS=3000)
        except Exception as ex:
            raise Exception(ex)
        self._database = None
        self._collection = None
        if database_name:
            self._database = self._collection[database_name]
        if collection_name:
            self._collection = self._database[collection_name]

    def get_database_names(self):
        """获取所有的数据库名称"""
        return self._connection.database_names

    def get_collection_names(self):
        """获取当前数据库的所有集合名称"""
        return self._database.collection_names(include_system_collections=False)

    def drop_collection(self, collection_name):
        """删除集合"""
        self._database.drop_collection(collection_name)

    def close(self):
        """关闭连接"""
        self._connection.close()

    def count(self):
        """获取当前集合的元素个数"""
        if self._collection:
            return self._collection.count()

    def find(self, filter, only_one=True, *args, **kwargs):
        """按条件查找数据"""
        if only_one:
            return self._collection.find_one(filter, *args, **kwargs)
        else:
            return self._collection.find(filter, *args, **kwargs)

    def remove(self, filter, only_one=True):
        """按条件删除数据"""
        if only_one:
            result = self._collection.delete_one(filter)
        else:
            result = self._collection.delete_many(filter)
        return result.deleted_count

    def add(self, resource, only_one=True):
        """添加元素"""
        if only_one:
            return self._collection.insert_one(resource)
        else:
            if not isinstance(resource, list):
                raise Exception("item should be list type.")
            return self._collection.insert_many(resource)


if __name__ == '__main__':
    mongo = MongoUtil(host='7.9.255.50', port='20000')
    print(mongo.count())
    mongo.close()

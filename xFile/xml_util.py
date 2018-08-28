#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 下午4:47
# @Author  : zhuhao
# @Project : xPython
# @File    : xml_util.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc: 使用xml.dom.minidom模块解析xml文件

'''
python解析XML常见的有三种方法：一是xml.dom.*模块,二是xml.sax.*模块，三是xml.etree.ElementTree模块(简称 ET)
XML相关术语：
1.Document(文档): 对应一个xml文件
2.Declaration(声明):
<?xml version="1.0" encoding="utf-8"?>
version指定了版本,encoding指定了文件编码
3.Comment（注释），同html中的注释
<!--just a comment about book_store-->
4.Element（元素）:指的是从（ 且包括） 开始标签直到
（ 且包括） 结束标签的部分，如<book_store></book_store>
<book_store name="newhua" website="https://www.amazon.cn/b?node=1876097071">
    <book1>
        <name>hamlet</name>
        <author>William Shakespeare</author>
    </book1>
</book_store>
5.Tag(标签): 用于表示素的起始与结束，如book1,name,author等
6.Attribute(属性),如上面的name,website
7.Text(文本),如hamelt
'''

from xml.dom import minidom


def getAttrName(node, attr_name):
    '''
    获取节点的属性值
    :param node:
    :param attr_name:
    :return:
    '''
    return node.getAttribute(attr_name) if node.hasAttribute(attr_name) else None


def getNodeValue(node, index=0):
    '''
    获取节点中第index个节点的值
    :param node:
    :param index:
    :return:
    '''
    return node.childNodes[index].nodeValue if node else None


def getNodes(node, name):
    '''
    获取节点下指定名称的所有子节点列表
    :param node:
    :param name:
    :return:
    '''
    return node.getElementsByTagName(name) if node else []


def getDatas(filename='movies.xml'):
    # 加载xml文件
    dom = minidom.parse(filename)
    # 获取xml文件的根节点
    root = dom.documentElement
    movies = getNodes(root, 'movie')
    movie_list = []
    for movie in movies:
        title = getAttrName(movie, 'title')
        node_type = getNodes(movie, 'type')
        node_format = getNodes(movie, 'format')
        node_year = getNodes(movie, 'year')
        node_rating = getNodes(movie, 'rating')
        node_stars = getNodes(movie, 'stars')
        node_description = getNodes(movie, 'rating')

        # 获取节点值
        type = getNodeValue(node_type[0])
        format = getNodeValue(node_format[0])
        year = getNodeValue(node_year[0])
        rating = getNodeValue(node_rating[0])
        stars = getNodeValue(node_stars[0])
        description = getNodeValue(node_description[0])

        movie_dict = dict()
        movie_dict['title'] = title
        movie_dict['type'] = type
        movie_dict['format'] = format
        movie_dict['year'] = year
        movie_dict['rating'] = rating
        movie_dict['stars'] = stars
        movie_dict['description'] = description

        movie_list.append(movie_dict)

    return movie_list


if __name__ == '__main__':
    movies = getDatas()
    for movie in movies:
        print(movie)

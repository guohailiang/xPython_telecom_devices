#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 下午6:36
# @Author  : zhuhao
# @Project : xPython
# @File    : abstract.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Version : V1.0
# @Desc:抽象类的实现

# 1.利用NotImplementedError,如果子类没有实现，只有在调用的时候才会抛弃NotImplementedError异常
class Payment(object):
    def pay(self):
        raise NotImplementedError


class ApplePay(Payment):
    def zhifu(self, money):
        print("ApplePay zhifu {0}.".format(money))


# 2.利用abc模块,如果子类没有实现abstract方法，在实例化的时候就会报错
from abc import ABCMeta, abstractmethod


class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()


class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return 3.14 * self._radius * self._radius


if __name__ == '__main__':
    # app=ApplePay()
    # app.zhifu(10)
    # app.pay()
    r1 = Rectangle(5, 4)
    r2 = Rectangle(4, 5)
    c1 = Circle(4)
    c2 = Circle(3)

    print(r1 >= r2, c1 > c2)

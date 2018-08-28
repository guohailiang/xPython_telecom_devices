#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 下午10:51
# @Author  : zhuhao
# @Project : helloPython
# @File    : timecost.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 使用with和time模块计算耗时

import time


class TimeCost:

    def __init__(self):
        self._start = time.time()
        self._end = self._start
        self._cost = 0

    def __enter__(self):
        return self

    def cost(self):
        self._end = time.time()
        self._cost = self._end - self._start
        return self._cost

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('finish')


if __name__ == '__main__':
    with TimeCost() as t:
        time.sleep(3)
        print(t.cost())

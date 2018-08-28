#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 下午10:58
# @Author  : zhuhao
# @Project : helloPython
# @File    : order_print.py
# @Contact : hyzhuhao891407@163.com 
# @Software : PyCharm
# @Desc: 三个线程顺序打印ABC

import threading

cond = threading.Condition()


class OrderPrint:
    """
    公共资源，加cond控制访问，current_num为当前打印的线程，1:A,2:B,3:C
    """

    def __init__(self, cond):
        self.cond = cond
        self.current_num = 1

    def printA(self):
        self.cond.acquire()
        while self.current_num != 1:
            self.cond.wait()
        print('A')
        self.current_num = 2
        self.cond.notifyAll()
        self.cond.release()

    def printB(self):
        self.cond.acquire()
        while self.current_num != 2:
            self.cond.wait()
        print('B')
        self.current_num = 3
        self.cond.notifyAll()
        self.cond.release()

    def printC(self):
        self.cond.acquire()
        while self.current_num != 3:
            self.cond.wait()
        print('C')
        self.current_num = 1
        self.cond.notifyAll()
        self.cond.release()


class ThreadA(threading.Thread):
    """
    线程A，执行打印A
    """

    def __init__(self, order_ins):
        self.order_ins = order_ins
        super(ThreadA, self).__init__()

    def run(self):
        self.order_ins.printA()


class ThreadB(threading.Thread):
    """
    线程B，执行打印B
    """

    def __init__(self, order_ins):
        self.order_ins = order_ins
        super(ThreadB, self).__init__()

    def run(self):
        self.order_ins.printB()


class ThreadC(threading.Thread):
    """
    线程C，执行打印C
    """

    def __init__(self, order_ins):
        self.order_ins = order_ins
        super(ThreadC, self).__init__()

    def run(self):
        self.order_ins.printC()


if __name__ == '__main__':
    order = OrderPrint(cond)
    for i in range(3):
        threadA = ThreadA(order)
        threadB = ThreadB(order)
        threadC = ThreadC(order)
        threadA.start()
        threadB.start()
        threadC.start()
        threadA.join()
        threadB.join()
        threadC.join()

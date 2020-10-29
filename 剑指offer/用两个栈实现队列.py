#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 0029 20:25
# @Author  : Letao
# @Site    : 
# @File    : 用两个栈实现队列.py
# @Software: PyCharm
# @desc    :


class CQueue(object):

    def __init__(self):
        self.sin = []
        self.sout = []


    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.sin.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        if len(self.sin) == 0 and len(self.sout) == 0:
            return -1
        elif len(self.sout) == 0:
            while self.sin:
                self.sout.append(self.sin.pop())
        return self.sout.pop()
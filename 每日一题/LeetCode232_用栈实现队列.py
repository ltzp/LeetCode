#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/05
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode232_用栈实现队列.py
# @Desc    :
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enter = []
        self.out = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.enter.append()

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.enter:
            self.out.append(self.enter.pop())
        value = self.out.pop()
        while self.out:
            self.enter.append(self.out.pop())
        return value


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.enter[0]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.enter:
            return True
        return False

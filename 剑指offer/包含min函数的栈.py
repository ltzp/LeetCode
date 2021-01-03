#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31
# @Author  : yuetao
# @Site    : 
# @File    : 包含min函数的栈.py
# @Desc    :
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        elif x < self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])


    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]


    def min(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.min())
    minStack.pop()
    print(minStack.top())
    print(minStack.min())


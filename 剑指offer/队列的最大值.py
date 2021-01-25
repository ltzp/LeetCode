#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/25
# @Author  : yuetao
# @Site    : 
# @File    : 队列的最大值.py
# @Desc    :
import collections
import heapq
class MaxQueue(object):

    def __init__(self):
        self.value = collections.deque()
        self.heap = []


    def max_value(self):
        """
        :rtype: int
        """
        if not self.value and not self.heap:
            return -1
        my_heap = []
        for i in self.heap:
            heapq.heappush(my_heap, i)
        return -heapq.nsmallest(1, my_heap)[0]



    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.value.append(value)
        self.heap.append(-value)


    def pop_front(self):
        """
        :rtype: int
        """
        if not self.value:
            return -1
        self.heap.pop(0)
        return self.value.popleft()

if __name__ == '__main__':
    solve = MaxQueue()
    solve.push_back(1)
    solve.push_back(2)
    print(solve.heap)
    print(solve.max_value())
    solve.pop_front()
    print(solve.max_value())

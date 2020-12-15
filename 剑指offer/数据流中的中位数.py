#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-01 21:20
# @Author  : Letao
# @Site    : 
# @File    : 数据流中的中位数.py
# @Software: PyCharm
# @desc    :
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big = [] #大顶堆，保存比较小的一半
        self.small = [] #小顶堆，保存比较大的一半



    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.big) != len(self.small):

            heapq.heappush(self.big, num)
            heapq.heappush(self.small, -heapq.heappop(self.big))
        else:
            heapq.heappush(self.small, -num)
            heapq.heappush(self.big, -heapq.heappop(self.small))



    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) != len(self.big):
            return self.big[0]
        else:
            return (self.big[0] - self.small[0]) /2.0

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/30
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode1046_最后一块石头的重量.py
# @Desc    :
import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        myheap = []
        for i in range(len(stones)):
            heapq.heappush(myheap, -stones[i])
        while len(myheap) >= 2:
            x = -(heapq.heappop(myheap))
            y = -(heapq.heappop(myheap))
            value = abs(x-y)
            heapq.heappush(myheap, -value)
        return -myheap[0]


if __name__ == '__main__':
    solve = Solution()
    stones = [2,7,4,1,8,1]
    result = solve.lastStoneWeight(stones)
    print(result)

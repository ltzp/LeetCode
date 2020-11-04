#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-04 22:48
# @Author  : Letao
# @Site    : 
# @File    : LeetCode56_合并区间.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return intervals
        intervals = sorted(intervals)
        length = len(intervals)
        res = [intervals[0]]
        for i in range(1, length):
            start, end = intervals[i]
            left, right = res[-1]
            if right < start:
                res.append(intervals[i])
            elif right == start:
                res.pop()
                res.append([left, end])
            else:
                left = min(left, start)
                right = max(right, end)
                res.pop()
                res.append([left, right])
        return res




if __name__ == "__main__":
    solve = Solution()
    intervals = [[1,4],[0,0]]
    result = solve.merge(intervals)
    print(result)
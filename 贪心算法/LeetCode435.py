#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-23 21:07
# @Author  : Letao
# @Site    : 
# @File    : LeetCode435.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda value:value[1])
        print(intervals)
        cur_location = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):

            if intervals[i][0] < cur_location:
                res += 1
            else:
                cur_location = intervals[i][1]
        return res

if __name__ == "__main__":
    solve = Solution()
    intervals = [ [1,2], [2,3] ]
    result = solve.eraseOverlapIntervals(intervals)
    print(result)
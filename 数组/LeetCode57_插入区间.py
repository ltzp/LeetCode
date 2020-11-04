#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-04 10:31
# @Author  : Letao
# @Site    : 
# @File    : LeetCode57_插入区间.py
# @Software: PyCharm
# @desc    :
"""
特殊情况没有处理
[1,5]
[0,0]
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        length = len(intervals)
        if length == 0:
            return [newInterval]
        res = []
        i = 0
        # 将没有交集的数据先放入结果中
        while i < length and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        left, right = newInterval
        # 进行合并的情况
        while i < length and intervals[i][0] <= newInterval[1]:
            left = min(left, intervals[i][0])
            right = max(right, intervals[i][1])
            i += 1
        res.append([left, right])
        # 将剩下的数据进行添加到结果
        res.extend(intervals[i:])
        return res



if __name__ == "__main__":
    solve = Solution()
    intervals = [[1,5]]
    newInterval = [0,0]
    result = solve.insert(intervals, newInterval)
    print(result)
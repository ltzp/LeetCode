#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-23 20:25
# @Author  : Letao
# @Site    : 
# @File    : LeetCode452_最少数量的剑引爆气球.py
# @Software: PyCharm
# @desc    :
"""
贪心算法，活动安排系列
"""
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda value:value[1])
        # print(points)
        location = points[0][1]
        res = 1
        for point in points:
            if location < point[0]:
                location = point[1]
                res += 1
        return res


if __name__ == "__main__":
    solve = Solution()
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    result = solve.findMinArrowShots(points)
    print(result)
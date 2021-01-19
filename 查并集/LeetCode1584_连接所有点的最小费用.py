#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/19
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode1584_连接所有点的最小费用.py
# @Desc    :
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        distance = [0] * length
        x1, y1 = points[0]
        visit = set()
        visit.add(0)
        for i in range(1, length):
            md = abs(points[i][0] - x1) + abs(points[i][1] - y1)
            distance[i] = md # 每一个点到第一个点的距离
        res = 0
        for j in range(length-1):
            the_min, idx = float("inf"), -1
            for k in range(length):
                if k not in visit and distance[k]< the_min:
                    the_min = distance[k]
                    idx = k
            visit.add(idx)
            res += the_min
            x_new, y_new = points[idx]
            for i in range(length):
                md = abs(points[i][0] - x_new) + abs(points[i][1] - y_new)
                distance[i] = min(distance[i], md)  # 更新距离
        return res


if __name__ == '__main__':
    solve = Solution()
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    result = solve.minCostConnectPoints(points)
    print(result)

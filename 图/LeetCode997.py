#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 0004 22:35
# @Author  : Letao
# @Site    : 
# @File    : LeetCode997.py
# @Software: PyCharm
# @desc    : 找到小镇的法官
# 两个数组记录每个点的出入度

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        res = -1
        if N == 1:
            return 1
        point_out = [0] * (N+1)
        point_in = [0] * (N+1)
        for point in trust:
            point_in[point[1]] += 1
            point_out[point[0]] += 1
        print(point_out)
        print(point_in)
        for i in range(len(point_in)):
            if point_in[i] == N - 1 and point_out[i] == 0:
                res = i
                break
        return res


if __name__ == "__main__":
    solve = Solution()
    N = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    result = solve.findJudge(N, trust)
    print(result)
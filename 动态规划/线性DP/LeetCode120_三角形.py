#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 0031 21:43
# @Author  : Letao
# @Site    : 
# @File    : LeetCode120.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        dp = [[] for i in range(length)]
        for i in range(length):
            for j in range(len(triangle[i])):
                dp[i].append(0)
        dp[0][0] = triangle[0][0]
        for i in range(1,length):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                    continue
                if j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j-1] + triangle[i][j]
                    continue
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]
        return min(dp[length-1])


if __name__ == "__main__":
    solve = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    result = solve.minimumTotal(triangle)
    print(result)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/04
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode354_俄罗斯套娃信封问题.py
# @Desc    :

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        length = len(envelopes)
        if length <= 1:
            return 1
        envelopes.sort(key=lambda x: x[0])
        print(envelopes)
        dp = [1 for i in range(length)]
        for i in range(1, length):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    solve = Solution()
    envelopes = [[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]
    result = solve.maxEnvelopes(envelopes)
    print(result)

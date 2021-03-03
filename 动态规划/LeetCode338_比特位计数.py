#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/03
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode338_比特位计数.py
# @Desc    :
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0 for i in range(num+1)]
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


if __name__ == '__main__':
    solve = Solution()
    num = int(input())
    result = solve.countBits(num)
    print(result)

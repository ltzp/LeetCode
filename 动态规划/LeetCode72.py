#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 0001 21:40
# @Author  : Letao
# @Site    : 
# @File    : LeetCode72.py
# @Software: PyCharm
# @desc    :当字符串 word1 的长度为 i，字符串 word2 的长度为 j 时，将 word1 转化为 word2 所使用的最少操作次数为 dp[i] [j]

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        length1 = len(word1)
        length2 = len(word2)
        dp = [[0 for i in range(length2 + 1)] for j in range(length1 + 1)]
        dp[0][0] = 0
        for i in range(1, length2+1):
            dp[0][i] = dp[0][i-1] + 1
        for i in range(1, length1+1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, length1+1):
            for j in range(1, length2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        return dp[length1][length2]


if __name__ == "__main__":
    solve = Solution()
    word1 = "horse"
    word2 = "ros"
    result = solve.minDistance(word1,word2)
    print(result)
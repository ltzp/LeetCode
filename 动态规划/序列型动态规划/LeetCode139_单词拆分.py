#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/09
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode139_单词拆分.py
# @Desc    :


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_dict = set(wordDict)
        length = len(s)
        if not s:
            return False
        dp = [False] * (length+1)
        dp[0] = True
        for i in range(1, length + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_dict:
                    dp[i] = True
                    break
        return dp[length]


if __name__ == '__main__':
    solve = Solution()
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    s = "catsandog"
    result = solve.wordBreak(s, wordDict)
    print(result)

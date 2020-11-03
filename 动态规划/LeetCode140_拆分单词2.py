#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-01 12:22
# @Author  : Letao
# @Site    : 
# @File    : LeetCode140_拆分单词2.py
# @Software: PyCharm
# @desc    :
"""
https://leetcode-cn.com/problems/word-break-ii/solution/140-dan-ci-chai-fen-shen-du-you-xian-sou-suo-by-n_/
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # 1.如果s中不存含有不存在wordDict的字母，直接返回[]
        self.res = []
        unique_char = set()
        for word in wordDict:
            for j in word:
                unique_char.add(j)
        for char in s:
            if char not in unique_char:
                return self.res
        self.dfs(s, "", wordDict)
        return self.res

    def dfs(self, s, now_str, wordDict):
        if len(s) == 0:
            self.res.append(now_str.strip())
            return
        for i in wordDict:
            if s.endswith(i):
                self.dfs(s[0:(len(s) - len(i))], ' '.join([i, now_str]), wordDict)
        return


if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    solve = Solution()
    result = solve.wordBreak(s, wordDict)
    print(result)

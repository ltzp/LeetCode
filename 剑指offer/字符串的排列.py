#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/06
# @Author  : yuetao
# @Site    : 
# @File    : 字符串的排列.py
# @Desc    :
class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(s, index, cur_s, used):
            if len(cur_s) == len(s):
                if cur_s not in result:
                    result.append(cur_s)
                return
            for i in range(0, len(s)):
                if not used[i]:
                    cur_s += s[i]
                    used[i] = True
                    dfs(s, index + 1, cur_s, used)
                    cur_s = cur_s[:-1]
                    used[i] = False

        result = []
        length = len(s)
        used = [False] * length
        dfs(s, 0, "", used)
        return result


if __name__ == '__main__':
    solve = Solution()
    s = "abc"
    result = solve.permutation(s)
    print(result)

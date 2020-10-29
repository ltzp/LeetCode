#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 0013 15:07
# @Author  : Letao
# @Site    : 
# @File    : LeetCode216_组合总和3.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.numCount = k
        self.target = n
        used = [False] * 10
        self.dfs([], used, 1)
        return self.res

    def dfs(self, path, used, cur_num):
        if len(path) > self.numCount:
            return
        if sum(path) > self.target:
            return
        if sum(path) == self.target:
            if len(path) == self.numCount:
                self.res.append(path[:])
                return
        for i in range(cur_num, 10):
            if used[i]:
                continue
            used[i] = True
            path.append(i)
            self.dfs(path, used, i+1)
            used[i] = False
            path.pop()




if __name__ == "__main__":
    solve = Solution()
    k = 3
    n = 9
    result = solve.combinationSum3(k, n)
    print(result)
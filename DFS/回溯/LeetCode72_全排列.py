#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 0008 17:23
# @Author  : Letao
# @Site    : 
# @File    : LeetCode72_全排列.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        path = []
        self.dfs(n, k , path,1)
        return  self.res

    def dfs(self, n , k ,path, start):
        if len(path) == k:
            #浅拷贝很重要
            self.res.append(path[:])
            return
        for i in range(start, n+1):
            path.append(i)
            self.dfs(n, k, path, i+1)
            path.pop()



if __name__ == "__main__":
    solve = Solution()
    # n = int(input())
    # k = int(input())
    n = 4
    k = 2
    result = solve.combine(n , k)
    print(result)
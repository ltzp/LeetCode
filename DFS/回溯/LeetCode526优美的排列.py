#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 0005 21:51
# @Author  : Letao
# @Site    : 
# @File    : LeetCode526优美的排列.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.res = 0
        #self.end = N
        path = []
        used = [False] * (N+1)
        self.dfs(N, used, path)
        return self.res

    def dfs(self, N, used, path):
        if len(path) == N:
            self.res += 1
            return
        for i in range(1, N+1):
            if used[i]:
                continue
            cur_index = len(path) + 1
            if i % cur_index == 0 or cur_index % i == 0:
                path.append(i)
                used[i] = True
                self.dfs(N, used, path)
                path.pop()
                used[i] = False


if __name__ == "__main__":
    solve = Solution()
    N = int(input())
    #N = 3
    result = solve.countArrangement(N)
    print(result)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-15 14:58
# @Author  : Letao
# @Site    : 
# @File    : 输出1-n无重复的偶数.py
# @Software: PyCharm
# @desc    :

class Solution(object):

    def deal(self, n):
        self.res = []
        self.nums = []
        for i in range(n+1):
            self.nums.append(i)
        self.used = [False] * (n + 1)
        self.dfs([])
        return self.res

    def dfs(self,  path):
        if len(path) == 5:
            if path[-1] % 2 == 0:
                mystr = ""
                for i in path:
                    mystr += str(i)
                self.res.append(int(mystr))
                return
        for i in range(1, len(self.nums)):
            if self.used[i]:
                continue
            self.used[i] = True
            path.append(self.nums[i])
            self.dfs(path)
            self.used[i] = False
            path.pop()


if __name__ == "__main__":
    solve = Solution()
    n = int(input())
    result = solve.deal(n)
    print(result)

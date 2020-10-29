#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 0030 21:41
# @Author  : Letao
# @Site    : 
# @File    : LeetCode18_四数之和.py
# @Software: PyCharm
# @desc    :

#TODO
"""
dfs 回溯超时
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.length = len(nums)
        self.used = [False for i in range(self.length)]
        self.params = sorted(nums)
        self.dfs(0, [], 0, target)
        return self.res

    def dfs(self, index, path, sum, target):

        if sum == target:
            if len(path) == 4:
                self.res.append(sorted(path[:]))
                return
        if index >= self.length:
            return
        if self.used[index]:
            return
        for i in range(index, self.length):
            if self.params[i] == self.params[i-1] and i > index:
                continue
            sum += self.params[i]
            path.append(self.params[i])
            self.used[i] = True
            self.dfs(i+1, path, sum, target)
            sum -= self.params[i]
            path.pop()
            self.used[i] = False


if __name__ == "__main__":
    solve = Solution()
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    result = solve.fourSum(nums, target)
    print(result)

    """

    [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    
    """
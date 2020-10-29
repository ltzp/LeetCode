#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 0029 0:12
# @Author  : Letao
# @Site    : 
# @File    : LeetCode78_子集.py
# @Software: PyCharm
# @desc    :
# TODO
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.used = [ False for i in range(len(nums))]
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums, index, path):
        sort_path = sorted(path)
        if sort_path not in self.res:
            self.res.append(path[:])
        if index >= len(nums):
            return
        if self.used[index]:
            return
        for i in range(index, len(nums)):
            self.used[i] = True
            path.append(nums[i])
            self.dfs(nums, i+1, path)
            path.pop()
            self.used[i] = False




if __name__ == "__main__":
    solve = Solution()
    nums = [1, 2, 3]
    result = solve.subsets(nums)
    print(result)
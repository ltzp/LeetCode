#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 0009 18:31
# @Author  : Letao
# @Site    : 
# @File    : LeetCode39_组合总数.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.aimed = target
        self.nums = candidates
        self.dfs([], 0)
        return self.res

    def dfs(self, path, all_sum):
        if all_sum > self.aimed:
            return
        if all_sum == self.aimed:
            new_path = path[:]
            new_path = sorted(new_path)
            if new_path in self.res:
                return
            else:
                self.res.append(new_path)
                return
        for i in self.nums:
            all_sum += i
            if all_sum > self.aimed:
                continue
            path.append(i)
            self.dfs(path, all_sum)
            all_sum -= i
            path.pop()


if __name__ == "__main__":
    solve = Solution()
    candidates = [3,4,7,8]
    target = 11
    result = solve.combinationSum(candidates, target)
    print(result)
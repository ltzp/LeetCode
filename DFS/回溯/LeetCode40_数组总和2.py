#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 0010 18:35
# @Author  : Letao
# @Site    : 
# @File    : LeetCode40_数组总和2.py
# @Software: PyCharm
# @desc    :
import collections
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.length = len(candidates)
        self.nums = sorted(candidates)
        self.aim = target
        used = [False] * self.length
        self.dfs(0, used, [], 0)
        return self.res

    def dfs(self, cur_index, used, path, all_sum):
        # if used[cur_index]:
        #     return

        if all_sum == self.aim:
            my_path = sorted(path)
            if my_path in self.res:
                return
            else:
                self.res.append(my_path)
                return
        for i in range(cur_index, self.length):
            all_sum += self.nums[i]
            if all_sum > self.aim or used[i]:
                all_sum -= self.nums[i]
                continue
            used[i] = True
            path.append(self.nums[i])
            self.dfs(cur_index+1, used, path, all_sum)
            used[i] = False
            all_sum -= self.nums[i]
            path.pop()

if __name__ == "__main__":
    solve = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    result = solve.combinationSum2(candidates, target)
    print(result)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/29
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode674_最长连续递增序列.py
# @Desc    :

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        queue = []
        res = 0
        for i in range(len(nums)):
            if not queue or nums[i] > nums[queue[-1]]:
                queue.append(i)
            else:
                count = 0
                while queue:
                    queue.pop()
                    count += 1
                res = max(res, count)
                queue.append(i)
        if queue:
            res = max(res, len(queue))
        return res


if __name__ == '__main__':
    solve = Solution()
    nums = [2,1,3]
    result = solve.findLengthOfLCIS(nums)
    print(result)

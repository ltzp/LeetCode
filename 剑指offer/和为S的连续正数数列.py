#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/19
# @Author  : yuetao
# @Site    : 
# @File    : 和为S的连续正数数列.py
# @Desc    :
"""
滑动窗口系列
"""

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        left,right = 1, 1
        windows_sum = 0
        res = []
        while left <= target/2:
            if windows_sum < target:
                windows_sum += right
                right += 1
            elif windows_sum > target:
                windows_sum -= left
                left += 1
            else:
                single_record = []
                for k in range(left, right):
                    single_record.append(k)
                res.append(single_record)
                windows_sum -= left
                left += 1
        return res



if __name__ == '__main__':
    solve = Solution()
    target = int(input())
    result = solve.findContinuousSequence(target)
    print(result)

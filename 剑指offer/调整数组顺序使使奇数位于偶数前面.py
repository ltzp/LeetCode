#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/30
# @Author  : yuetao
# @Site    : 
# @File    : 调整数组顺序使使奇数位于偶数前面.py
# @Desc    :
"""
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
"""


class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [None] * length
        start, end = 0, length-1
        for i in range(length):
            if nums[i] & 1:
                res[start] = nums[i]
                start += 1
            else:
                res[end] = nums[i]
                end -= 1
        return res


if __name__ == '__main__':
    solve = Solution()
    nums = [1, 2, 3, 4]
    result = solve.exchange(nums)
    print(result)

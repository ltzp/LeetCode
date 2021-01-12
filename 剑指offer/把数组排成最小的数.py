#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/10
# @Author  : yuetao
# @Site    : 
# @File    : 把数组排成最小的数.py
# @Desc    :
"""
排序问题
"30"， "3"，"34"，"5"， "9"

"""

import functools
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        strs =[str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(self.get_min_nums))
        return ''.join(strs)


    def get_min_nums(self, num1, num2):
        a, b = num1 + num2, num2 + num1
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0



if __name__ == '__main__':
    solve = Solution()
    nums = [3,30,34,5,9]
    result = solve.minNumber(nums)
    print(result)

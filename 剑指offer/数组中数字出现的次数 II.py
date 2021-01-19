#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/16
# @Author  : yuetao
# @Site    : 
# @File    : 数组中数字出现的次数 II.py
# @Desc    :
"""
将每一个数转为二进制，统计每一位上1的个数，然后取余
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            count = 0
            bit = 1 << i
            for num in nums:
                if num & bit != 0:
                    count += 1
            if count % 3 != 0:
                res |= bit
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res


if __name__ == '__main__':
    solve = Solution()
    nums = [9,1,7,9,7,9,7]
    result = solve.singleNumber(nums)
    print(result)

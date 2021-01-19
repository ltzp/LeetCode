#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/16
# @Author  : yuetao
# @Site    : 
# @File    : 数组中数字出现的次数.py
# @Desc    :
class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        length = len(nums)
        start = 0
        res = []
        while start < length:
            if start + 1 < length:
                if not nums[start] ^ nums[start+1]:
                    start += 2
                else:
                    res.append(nums[start])
                    start += 1
            else:
                if len(res) < 2:
                    res.append(nums[start])
                    start += 1
        return res

    """
    优化方法->异或运算
    """
    def singleNumbersTwo(self, nums):
        ret = 0
        for i in nums:
            ret ^= i
        div = 1
        while (ret & div) == 0:
            div <<= 1
        a, b = 0, 0
        for num in nums:
            if (num & div) != 0:
                a ^= num
            else:
                b ^= num
        return [a, b]


if __name__ == '__main__':
    nums = [1,6]
    solve = Solution()
    result = solve.singleNumbersTwo(nums)
    print(result)
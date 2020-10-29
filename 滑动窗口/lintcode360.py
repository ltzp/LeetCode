#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 0015 19:12
# @Author  : Letao
# @Site    : 
# @File    : lintcode360.py
# @Software: PyCharm
# @desc    :

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        window = []
        left , right = 0, 0
        length = len(nums)
        res = []
        while right < length:
            cur_num = nums[right]
            right += 1
            if len(window) < k:
                window.append(cur_num)
            while len(window) == k:
                record = sorted(window)
                if k % 2 == 1:
                    mid = int(k/2)
                else:
                    mid = k/2 -1
                res.append(record[mid])
                move_int = nums[left]
                left += 1
                window.pop(0)
        return res

if __name__ == "__main__":
    solve = Solution()
    nums = [1,2,7,7,2,10,3,4,5]
    k = 2
    result = solve.medianSlidingWindow(nums, k)
    print(result)
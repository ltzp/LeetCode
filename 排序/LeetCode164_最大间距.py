#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-26 20:23
# @Author  : Letao
# @Site    : 
# @File    : LeetCode164_最大间距.py
# @Software: PyCharm
# @desc    :

"""
桶排序：桶的长度，桶的个数，每个元算在哪个桶
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        num_min = min(nums)
        num_max = max(nums)
        max_gap = 0
        each_bucket_len = max(1, (num_max - num_min) // (len(nums) - 1)) #桶的长度
        buckets = [[] for _ in range((num_max - num_min) // each_bucket_len + 1)] # 桶的个数
        # print(each_bucket_len)
        # print(buckets)
        for i in range(len(nums)):
            loc = (nums[i] - num_min) // each_bucket_len
            buckets[loc].append(nums[i])
        prev_max = float("inf")
        for i in range(len(buckets)):
            if buckets[i] and prev_max != float("inf"):
                max_gap = max(max_gap, min(buckets[i]) - prev_max)
            if buckets[i]:
                prev_max = max(buckets[i])
        return max_gap



if __name__ == "__main__":
    solve = Solution()
    nums = [3,6,9,1]
    result = solve.maximumGap(nums)
    print(result)
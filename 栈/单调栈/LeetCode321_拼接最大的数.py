#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-12-02 20:40
# @Author  : Letao
# @Site    : 
# @File    : LeetCode321_拼接最大的数.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        dp = [None] * k
        start1 = 0
        start2 = 0
        for i in range(k):
            if start1 < len(nums1) and start2 < len(nums2):
                dp[i] = max(max(nums1[start1:]), max(nums2[start2:]))
                if dp[i] == max(nums1[start1:]):
                    start1 = nums1.index(dp[i]) + 1
                if dp[i] == max(nums2[start2:]):
                    start2 = nums2.index(dp[i]) + 1
                continue
            if start1 == len(nums1) and start2 < len(nums2):
                if len(nums2) - start2 <= k - i:
                    dp[i] = nums2[start2]
                    start2 += 1
                else:
                    dp[i] = max(nums2[start2:])
                    start2 = nums2.index(dp[i]) + 1
                continue
            if start1 < len(nums1) and start2 == len(nums2):
                if len(nums2) - start2 <= k - i:
                    dp[i] = nums1[start1]
                    start1 += 1
                else:
                    dp[i] = max(nums1[start1:])
                    start1 = nums1.index(dp[i]) + 1
                continue

        return dp




if __name__ == "__main__":
    solve = Solution()
    # nums1 = [3, 4, 6, 5]
    # nums2 = [9, 1, 2, 5, 8, 3]
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    result = solve.maxNumber(nums1, nums2, k)
    print(result)
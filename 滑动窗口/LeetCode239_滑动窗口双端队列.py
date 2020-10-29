#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 0015 21:18
# @Author  : Letao
# @Site    : 
# @File    : LeetCode239_滑动窗口双端队列.py
# @Software: PyCharm
# @desc    :
import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return nums
        res = [0] * (length - k + 1)
        dq = collections.deque()
        for i in range(length):
            #1.头 队列的长度是否等于K,如果对面满足K的大小就需要出队
            if dq and dq[0] == i - k:
                dq.popleft()
            #2. 尾 从队尾把比将要插入的值小的去掉
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            #3.尾 尾部插入值
            dq.append(i)
            #4.头 在头部取最大值
            if i >= k - 1:
                res[i-k+1] = nums[dq[0]]
        return res

if __name__ == "__main__":
    solve = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = solve.maxSlidingWindow(nums, k)
    print(result)
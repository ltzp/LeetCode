#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 0020 21:25
# @Author  : Letao
# @Site    : 
# @File    : 圆环切割.py
# @Software: PyCharm
# @desc    :
import sys

class Solution:

    def split_arr(self, count, nums_arr):
        my_sum = sum(nums_arr)
        if my_sum & 1:
            return "NO"
        window = 0
        left, right = 0, 0
        mid = int(my_sum/2)
        while right < count:
            cur_num = int(nums_arr[right])
            right += 1
            window += cur_num
            if window == mid:
                return "YES"
            while window > mid and left < right:
                move_num = int(nums_arr[left])
                left += 1
                window -= move_num
                if window == mid:
                    return "YES"
        return "NO"


if __name__ == "__main__":
    solve = Solution()
    T = int(input())
    for i in range(T):
        n = int(input())
        nums = input().split()
        nums = [int(i) for i in nums]
        print(solve.split_arr(n, nums))

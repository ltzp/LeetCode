#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 0020 23:47
# @Author  : Letao
# @Site    : 
# @File    : 堆积木.py
# @Software: PyCharm
# @desc    :

class Solution:
    def deal(self, n, m ,nums):
        get_sum = 0
        for i in range(n):
            get_sum += nums[i]
            if get_sum + m < i*(i+1)/2:
                return "NO"
        return "YES"




if __name__ == "__main__":
    solve = Solution()
    T = int(input())
    for i in range(T):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        nums = input().split()
        nums = [int(i) for i in nums]
        print(solve.deal(n, m ,nums))
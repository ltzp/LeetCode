#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/26
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode1011_在D天内送达包裹的能力.py
# @Desc    :

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            cur_day, cur_weight = 1, 0
            for weight in weights:
                if cur_weight + weight > mid:
                    cur_day += 1
                    cur_weight = 0
                cur_weight += weight
            if cur_day <= D:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solve = Solution()
    weights = [1,2,3,4,5,6,7,8,9,10]
    D = 5
    result = solve.shipWithinDays(weights, D)
    print(result)

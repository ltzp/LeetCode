#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/16
# @Author  : yuetao
# @Site    : 
# @File    : 贪吃的小Q.py
# @Desc    :
import sys
class Solution(object):

    def solve(self, N, M):
        low, higt = 1, M
        while low <= higt:
            mid = (low + higt)//2
            if self.my_sum(mid, N) == M:
                return mid
            elif self.my_sum(mid, N) < M:
                low = mid + 1
            else:
                higt = mid - 1
        if low > higt:
            return low - 1
        return 0

    def my_sum(self, s, n):
        total_sum = 0
        for i in range(n):
            total_sum += s
            s = (s+1)//2
        return total_sum


if __name__ == '__main__':
    solution = Solution()
    line = sys.stdin.readline().strip()
    nums = list(map(int, line.split()))
    result = solution.solve(nums[0], nums[1])
    print(result)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-18 18:48
# @Author  : Letao
# @Site    : 
# @File    : LeetCode134_加油站.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # total记录可获得的总油量-总油耗， cur记录当前油耗情况， ans记录出发位置
        total, cur, ans = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                ans = i + 1
        if total >= 0:
            return ans
        else:
            return -1



if __name__ == "__main__":
    solve = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    result = solve.canCompleteCircuit(gas, cost)
    print(result)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-25 21:57
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1217_玩筹码.py
# @Software: PyCharm
# @desc    :

from collections import defaultdict
class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        hash_record = defaultdict(int)
        for i in position:
            hash_record[i] += 1
        sorted(hash_record)
        # print(hash_record)
        one_value = 0
        two_value = 0
        for key,value in hash_record.items():
            if key & 1:
                one_value += value
            else:
                two_value += value
        return two_value if one_value > two_value else one_value


if __name__ == "__main__":
    solve = Solution()
    position = [1,2,3]
    result = solve.minCostToMoveChips(position)
    print(result)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 0004 23:02
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1042.py
# @Software: PyCharm
# @desc    : 不邻接植花
# https://leetcode-cn.com/problems/flower-planting-with-no-adjacent/

from collections import defaultdict
class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        if paths == []:
            return [1] * N
        point_hash = defaultdict(list)
        for i in paths:
            point_hash[i[0]-1].append(i[1]-1)
            point_hash[i[1]-1].append(i[0]-1)
        res = [0] * N
        for i in range(len(res)):
            #相邻的点
            areas = point_hash.get(i)
            choice_flower = set({1, 2, 3, 4})
            print(areas)
            if not areas:
                res[i] = choice_flower.pop()
            else:
                for area in areas:
                    if res[area] in choice_flower:
                        choice_flower.remove(res[area])
                res[i] = choice_flower.pop()
        return res


if __name__ == "__main__":
    solve = Solution()
    N = 10000
    paths = [[1,2]]
    result = solve.gardenNoAdj(N, paths)
    print(result)
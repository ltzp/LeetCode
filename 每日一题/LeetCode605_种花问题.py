#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/01
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode605_种花问题.py
# @Desc    :

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        record = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        for i,value in enumerate(flowerbed):
            if value == 0:
                if 0 < i < len(flowerbed) - 1:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        record += 1
                if i == 0:
                    if len(flowerbed) > 1 :
                        if flowerbed[i+1] == 0:
                            flowerbed[i] = 1
                            record += 1
                    else:
                        if flowerbed[i] == 0:
                            flowerbed[i] = 1
                            record += 1
                if i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        record += 1
            if record >= n:
                return True
        return False


if __name__ == '__main__':
    solve = Solution()
    flowerded = [0,1,0]
    n = 1
    result = solve.canPlaceFlowers(flowerded, n)
    print(result)

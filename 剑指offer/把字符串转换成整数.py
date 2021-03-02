#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/30
# @Author  : yuetao
# @Site    : 
# @File    : 把字符串转换成整数.py
# @Desc    :
class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        res, i, sign = 0, 1, 1
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if str[0] == '-':
            sign = -1
        elif str[0] != '+':
            i = 0
        for c in str[i:]:
            if not '0' <= c <= '9': break
            if res > bndry or res == bndry and c > '7': return int_max if sign == 1 else int_min
            res = 10 * res + ord(c) - ord('0')
        return sign * res



if __name__ == '__main__':
    solve = Solution()
    str = input()
    result = solve.strToInt(str)
    print(result)

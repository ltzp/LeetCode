#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/10
# @Author  : yuetao
# @Site    : 
# @File    : 数字序列中某一位的数字.py
# @Desc    :
"""
1 位：1-9， 占9位
2 位：10-99 占180位
3 位  100-999 900*3位

"""

class Solution(object):

    """
    超时
    """
    def my_findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = "0"
        record = 1
        start = 1
        while record < n + 1:
            s += str(start)
            record = len(s)
            start += 1
        return s[n:n+1]

    def findNthDigit(self, n):
        if n == 0:
            return 0
        digit = 1 #当前位数
        start = 1 #起点
        index_count = digit * 9 * start # 每个位数包含最大的个数
        while n > index_count:
            n -= index_count
            digit += 1
            start *= 10
            index_count = digit * 9 * start
        num = start + (n - 1) / digit
        remain = (n - 1) % digit
        s_num = str(num)
        return int(s_num[remain: remain+ 1])


if __name__ == '__main__':
    solve = Solution()
    n = int(input())
    result = solve.findNthDigit(n)
    print(result)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/25
# @Author  : yuetao
# @Site    : 
# @File    : 圆圈中最后剩下的数字.py
# @Desc    :

class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        record = [i for i in range(n)]
        start = 0
        while len(record) > 1:
            index = m % len(record)
            delete_index = (start + index - 1) % len(record)
            record.pop(delete_index)
            start = delete_index
        return record[0]



if __name__ == '__main__':
    solve = Solution()
    n = 10
    m = 17
    result = solve.lastRemaining(n, m)
    print(result)

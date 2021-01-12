#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/10
# @Author  : yuetao
# @Site    : 
# @File    : 第一个只出现一次的字符.py
# @Desc    :
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return " "
        length = len(s)
        record_map = collections.defaultdict(list)
        for i in range(length):
            record_map[s[i]].append(i)
        print(record_map)
        res = " "
        single_list = []
        for key,value in record_map.items():
            if len(value) == 1:
                single_list.append(value[0])
        single_list.sort()
        if not single_list:
            return res
        return single_list[0]



if __name__ == '__main__':
    solve = Solution()
    s = "cc"
    result = solve.firstUniqChar(s)
    print(result)

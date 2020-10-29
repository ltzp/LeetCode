#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 0014 18:26
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1002_查找常用字符.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if not A:
            return A
        record = A[0]
        record_map = {}
        for i in record:
            if i not in record_map:
                record_map[i] = 1
            else:
                record_map[i] += 1
        length = len(A)
        res = []
        for key,value in record_map.items():
            flag = False
            if value == 1:
                for j in range(1, length):
                    if A[j].count(key) >= value:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    res.append(key)
            else:
                count_min = value
                for j in range(1, length):
                    if A[j].count(key) == 0:
                        count_min = 0
                        flag = False
                        break
                    elif A[j].count(key) <= count_min:
                        count_min = A[j].count(key)
                        flag = True
                    else:
                        flag = True
                for i in range(count_min):
                    res.append(key)
        return res





if __name__ == "__main__":
    solve = Solution()
    A = ["dbaabcba","cabcdbab","cdbcbdad","abadbacc","bdddddaa","daddabab","baaaddaa","dccdaabd"]
    result = solve.commonChars(A)
    print(result)
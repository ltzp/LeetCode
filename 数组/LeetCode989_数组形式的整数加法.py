#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/22
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode989_数组形式的整数加法.py
# @Desc    :
"""
用一个标志，进行是否是进位判断
"""

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        k_arr = []
        if K == 0:
            k_arr.append(K)
        else:
            while K > 0:
                k_arr.append(K % 10)
                K = int(K/10)
        a_arr = A[::-1]
        a_left,k_left = 0, 0
        res = []
        flag = False
        while a_left < len(a_arr) and k_left < len(k_arr):
            if flag:
                sum_num = a_arr[a_left] + k_arr[k_left] + 1
                flag = False
            else:
                sum_num = a_arr[a_left] + k_arr[k_left]
            if sum_num >= 10:
                flag = True
            res.append(sum_num%10)
            a_left += 1
            k_left += 1
        while a_left < len(a_arr):
            sum_num = a_arr[a_left]
            if flag:
                sum_num = sum_num + 1
                flag = False
            if sum_num >= 10:
                flag = True
            res.append(sum_num%10)
            a_left += 1
        while k_left < len(k_arr):
            sum_num = k_arr[k_left]
            if flag:
                sum_num = sum_num + 1
                flag = False
            if sum_num >= 10:
                flag = True
            res.append(sum_num%10)
            k_left += 1
        if flag:
            res.append(1)
        return res[::-1]


if __name__ == '__main__':
    solve = Solution()
    A = [6]
    K = 809
    result = solve.addToArrayForm(A, K)
    print(result)

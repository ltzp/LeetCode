#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-15 21:14
# @Author  : Letao
# @Site    : 
# @File    : LeetCode402_移掉K位数字.py
# @Software: PyCharm
# @desc    :
"""
ps:删除的几位数字不一定是连续的
"""


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        result = ""
        for i in range(len(num)):
            cur_vaule = ord(num[i]) - ord('0')
            while len(stack) != 0 and stack[len(stack)-1] > cur_vaule and k > 0:
                stack.pop()
                k -= 1
            if cur_vaule != 0 or len(stack) != 0:
                stack.append(cur_vaule)
        while len(stack)!=0 and k>0:
            stack.pop()
            k -= 1
        print(stack)
        for i in range(len(stack)):
            result += str(stack[i])
        if result == "":
            return "0"
        return result

if __name__ == "__main__":
    solve = Solution()
    # num = input()
    # k = int(input())

    num = "5337"
    k = 2
    result = solve.removeKdigits(num, k)
    print(result)
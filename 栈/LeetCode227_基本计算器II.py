#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/11
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode227_基本计算器II.py
# @Desc    :
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        stack = []
        num = 0
        preSign = "+"
        for i in range(length):
            if s[i] != " " and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == length - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/num))
                preSign = s[i]
                num = 0
        return sum(stack)


if __name__ == '__main__':
    solve = Solution()
    s = "14-3/2"
    result = solve.calculate(s)
    print(result)

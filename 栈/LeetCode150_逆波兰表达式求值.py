#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/20
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode150_逆波兰表达式求值.py
# @Desc    :

import sys

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        number_stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/":
                number_one = number_stack.pop()
                number_two = number_stack.pop()
                number = 0
                if tokens[i] == "+":
                    number = number_two + number_one
                if tokens[i] == "-":
                    number = number_two - number_one
                if tokens[i] == "*":
                    number = number_two * number_one
                if tokens[i] == "/":
                    number = number_two/number_one
                number_stack.append(int(number))
            else:
                number_stack.append(int(tokens[i]))
        return number_stack[-1]


if __name__ == '__main__':
    solve = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = solve.evalRPN(tokens)
    print(result)

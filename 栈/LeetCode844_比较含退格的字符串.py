#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 0019 18:28
# @Author  : Letao
# @Site    : 
# @File    : LeetCode844_比较含退格的字符串.py
# @Software: PyCharm
# @desc    :

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_S = []
        stack_T = []
        length_S = len(S)
        length_T = len(T)
        for i in range(length_S):
            if S[i] != '#':
                stack_S.append(S[i])
            else:
                if stack_S:
                    stack_S.pop()
        for j in range(length_T):
            if T[j] != '#':
                stack_T.append(T[j])
            else:
                if stack_T:
                    stack_T.pop()
        print(stack_S)
        print(stack_T)
        if stack_T == stack_S:
            return True
        return False




if __name__ == "__main__":
    solve = Solution()
    # S = input()
    # T = input()
    S = "xywrrmp"
    T = "xywrrmu#p"
    result = solve.backspaceCompare(S, T)
    print(result)
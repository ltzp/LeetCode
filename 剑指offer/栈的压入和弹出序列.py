#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/01
# @Author  : yuetao
# @Site    : 
# @File    : 栈的压入和弹出序列.py
# @Desc    :
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if not pushed and not popped:
            return True
        elif not pushed and popped:
            return False
        elif pushed and not popped:
            return False
        push_length = len(pushed)
        pop_length = len(popped)
        push_index, pop_index = 0, 0
        stack = []
        while pop_index <= pop_length - 1 and push_index <= push_length - 1:
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
            if pushed[push_index] != popped[pop_index]:
                #stack 加入数据
                stack.append(pushed[push_index])
                push_index += 1
                #stack pop 数据
            elif pushed[push_index] == popped[pop_index]:
                push_index += 1
                pop_index += 1
        while stack:
            if stack.pop() == popped[pop_index]:
                pop_index += 1
            else:
                return False
        else:
            return True


if __name__ == '__main__':
    solve = Solution()
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    result = solve.validateStackSequences(pushed, popped)
    print(result)

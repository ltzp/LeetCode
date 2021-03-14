#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/12
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode331_验证二叉树的前序序列化.py
# @Desc    :

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorders = preorder.split(",")
        print(preorders)
        stack = []
        for i in range(len(preorders)):
            stack.append(preorders[i])
            while stack and len(stack) >= 3 and stack[-1] == stack[-2] and stack[-1] == '#':
                stack.pop()
                stack.pop()
                if stack[-1] == '#':
                    return False
                stack.pop()
                stack.append('#')
        if len(stack) == 1 and stack[0] == '#':
            return True
        return False


if __name__ == '__main__':
    solve = Solution()
    preorder = "1,#,#,#,#"
    result = solve.isValidSerialization(preorder)
    print(result)

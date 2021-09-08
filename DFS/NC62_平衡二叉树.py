#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/09/08
# @Author  : yuetao
# @Site    : 
# @File    : NC62_平衡二叉树.py
# @Desc    :

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.res = True
        self.dfs(pRoot)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left) + 1
        right = self.dfs(node. right) + 1
        if abs(left - right) > 1:
            self.res=False
        return max(left, right)




if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    f = TreeNode(5)

    a.left = b
    a.right = c
    b.left = d
    d.left = f
    solve = Solution()
    res = solve.IsBalanced_Solution(a)
    print(res)

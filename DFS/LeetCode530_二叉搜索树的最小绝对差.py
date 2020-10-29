#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 0012 19:14
# @Author  : Letao
# @Site    : 
# @File    : LeetCode530_二叉搜索树的最小绝对差.py
# @Software: PyCharm
# @desc    :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float("inf")
        self.path = []
        self.dfs(root)
        length = len(self.path)
        for i in range(1, length):
            self.res = min(self.res, abs(self.path[i] - self.path[i-1]))
        return self.res

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.path.append(node.val)
        self.dfs(node.right)


if __name__ == "__main__":
    a = TreeNode(236)
    b = TreeNode(104)
    c = TreeNode(701)
    d = TreeNode(227)
    e = TreeNode(911)
    a.left = b
    a.right = c
    b.right = d
    c.right = e
    solve = Solution()
    result = solve.getMinimumDifference(a)
    print(result)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 0010 20:56
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1123.py
# @Software: PyCharm
# @desc    :最深叶节点的最近公共祖先

class TreeNode(object):


    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    max_dept = 0
    res = []
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        self.dfs(root, 0)
        return self.res
    def dfs(self, node, dept):
        if not node:
            return 0
        dept += 1
        left = self.dfs(node.left, dept)
        right = self.dfs(node.right, dept)
        if left == right and dept >= self.max_dept:
            self.res.append(node)
            self.max_dept = dept
        return max(left, right)


if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    result = solve.lcaDeepestLeaves(a)
    print(result)
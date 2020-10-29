#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 0011 20:41
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1026_结点与祖先之间的最大差值.py
# @Software: PyCharm
# @desc    : 记录最大值和最小值

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    res = 0

    def maxAncestorDiff(self, root):
        if not root:
            return 0
        self.dfs(root, root.val, root.val)
        return self.res

    def dfs(self, root, maxValue, minValue):
        if not root:
            return
        maxValue = max(root.val, maxValue)
        minValue = min(root.val, minValue)
        if root.left is None and root.right is None:
            self.res = max(self.res, abs(maxValue - minValue))
        self.dfs(root.left, maxValue, minValue)
        self.dfs(root.right, maxValue, minValue)


if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(8)
    b = TreeNode(3)
    c = TreeNode(10)
    d = TreeNode(1)
    e = TreeNode(6)
    f = TreeNode(14)
    g = TreeNode(4)
    h = TreeNode(7)
    i = TreeNode(13)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = g
    e.right = h
    c.right = f
    f.left = i
    result = solve.maxAncestorDiff(a)
    print(result)

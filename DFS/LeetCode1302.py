#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 0006 21:58
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1302.py
# @Software: PyCharm
# @desc    :
# https://leetcode-cn.com/problems/deepest-leaves-sum/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    max_dept = 1
    res = 0

    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dept = 1
        self.dfs(root, dept)
        return self.res

    def dfs(self, node, dept):
        if not node:
            return 0
        if dept > self.max_dept:
            self.max_dept = dept
        if not node.left and not node.right and dept == self.max_dept:
            self.res += node.val
        if node.left:
            self.dfs(node.left, dept + 1)
        if node.right:
            self.dfs(node.right, dept + 1)


if __name__ == "__main__":
    a = TreeNode(1)
    # b = TreeNode(2)
    # c = TreeNode(3)
    # d = TreeNode(4)
    # e = TreeNode(5)
    # f = TreeNode(6)
    # g = TreeNode(7)
    # h = TreeNode(8)
    solve = Solution()
    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.right = f
    # d.left = g
    # f.right = h
    result = solve.deepestLeavesSum(a)
    print(result)

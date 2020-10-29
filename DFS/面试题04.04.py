#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 0002 22:23
# @Author  : Letao
# @Site    : 
# @File    : 面试题04.04.py
# @Software: PyCharm
# @desc    : 判断是否是平衡二叉树

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        arr = []
        dep = float("-inf")
        self.dfs(root, arr)
        if not arr:
            return True
        else:
            return False

    def dfs(self, node, arr):
        if not node:
            return 0
        left_dept = self.dfs(node.left, arr)
        right_dept = self.dfs(node.right, arr)
        if abs(left_dept - right_dept) > 1:
            arr.append(abs(left_dept - right_dept))
        dept = max(left_dept, right_dept)
        return dept + 1
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 0005 21:57
# @Author  : Letao
# @Site    : 
# @File    : LeetCode337.py
# @Software: PyCharm
# @desc    : 巧妙的运用DFS
# https://leetcode-cn.com/problems/house-robber-iii/

# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))

    def dfs(self, node):
        if not node:
            return 0, 0
        left = self.dfs(node.left)
        print(left)
        right = self.dfs(node.right)
        print(right)
        #偷当前结点，则左右子树都不能偷
        v1 = node.val + left[1] + right[1]
        #不偷当前结点，则取左右结点树中的最大值
        v2 = max(left) + max(right)
        return v1, v2

if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(3)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(3)
    e = TreeNode(1)
    a.left = b
    a.right = c
    b.right = d
    c.right = e
    result = solve.rob(a)
    print(result)
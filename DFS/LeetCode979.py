#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 0010 20:42
# @Author  : Letao
# @Site    : 
# @File    : LeetCode979.py
# @Software: PyCharm
# @desc    :


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = 0

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.res += abs(left) + abs(right)
        return node.val + left + right - 1


if __name__=="__main__":
    solve = Solution()
    a = TreeNode(1)
    b = TreeNode(0)
    c = TreeNode(0)
    d = TreeNode(3)
    a.left = b
    a.right = c
    b.right = c
    result = solve.distributeCoins(a)
    print(result)
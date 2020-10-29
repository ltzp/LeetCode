#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 0002 18:41
# @Author  : Letao
# @Site    : 
# @File    : LeetCode872.py
# @Software: PyCharm
# @desc    : 叶子相似的树

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1, res2 = list(), list()
        self.dfs(root1, res1)
        self.dfs(root2, res2)
        print(res1)
        print(res2)
        if len(res1) != len(res2):
            return False
        for i in range(len(res1)):
            if res1[i] != res2[i]:
                return False
        return True

    def dfs(self, node, res):
        if not node.left and not node.right:
            res.append(node.val)
            return
        if node.left:
            self.dfs(node.left, res)
        if node.right:
            self.dfs(node.right, res)


if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(1)
    d = TreeNode(6)
    e = TreeNode(2)
    f = TreeNode(9)
    g = TreeNode(8)
    h = TreeNode(7)
    i = TreeNode(4)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i
    result = solve.leafSimilar(a, c)
    print(result)


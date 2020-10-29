#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 0004 17:47
# @Author  : Letao
# @Site    : 
# @File    : LeetCode1315.py
# @Software: PyCharm
# @desc    : 祖父节点值为偶数的节点和
# https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    result = 0

    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node:
            return
        if node.val % 2 == 1:
            if node.left:
                self.dfs(node.left)
            if node.right:
                self.dfs(node.right)
        else:
            if node.left:
                if node.left.left:
                    self.result += node.left.left.val
                if node.left.right:
                    self.result += node.left.right.val
                self.dfs(node.left)
            if node.right:
                if node.right.left:
                    self.result += node.right.left.val
                if node.right.right:
                    self.result += node.right.right.val
                self.dfs(node.right)

if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(6)
    b = TreeNode(7)
    c = TreeNode(8)
    d = TreeNode(2)
    e = TreeNode(7)
    f = TreeNode(1)
    g = TreeNode(3)
    h = TreeNode(9)
    i = TreeNode(1)
    j = TreeNode(4)
    k = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    e.left = i
    e.right = j
    g.right = k
    result = solve.sumEvenGrandparent(a)
    print(result)


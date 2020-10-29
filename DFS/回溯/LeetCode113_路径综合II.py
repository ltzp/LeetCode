#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 0026 13:43
# @Author  : Letao
# @Site    : 
# @File    : LeetCode113_路径综合II.py
# @Software: PyCharm
# @desc    :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.targt = sum
        self.res = []
        self.dfs(root, [], 0)
        return self.res

    def dfs(self, node, path, sum):
        if not node:
            return
        sum += node.val
        path.append(node.val)
        if not node.left and not node.right and sum == self.targt:
            self.res.append(path[:])
        self.dfs(node.left, path, sum)
        self.dfs(node.right, path, sum)
        sum -= node.val
        path.pop()




if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    f = TreeNode(13)
    g = TreeNode(4)
    h = TreeNode(7)
    i = TreeNode(2)
    j = TreeNode(5)
    k = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    c.left = f
    c.right = g
    d.left = h
    d.right = i
    g.left = j
    g.right = k
    sum = 22
    result = solve.pathSum(a, sum)
    print(result)
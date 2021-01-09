#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/06
# @Author  : yuetao
# @Site    : 
# @File    : 二叉树中的和为某一值的路径.py
# @Desc    :
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
        self.res = []
        self.target = sum
        self.dfs(root, [], 0)
        return self.res

    def dfs(self, node, path, sum):
        if not node:
            return
        path.append(node.val)
        sum += node.val
        if not node.left and not node.right:
            if sum == self.target:
                self.res.append(path[:])
        self.dfs(node.left, path, sum)
        self.dfs(node.right, path, sum)
        sum -= node.val
        path.pop()




if __name__ == '__main__':
    solve = Solution()
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(13)
    f = TreeNode(4)
    g = TreeNode(7)
    h = TreeNode(2)
    i = TreeNode(5)
    j = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    d.left = g
    d.right = h
    c.left = e
    c.right = f
    f.left = i
    f.right = j
    sum = 22
    result = solve.pathSum(a, sum)
    print(result)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 0027 23:12
# @Author  : Letao
# @Site    : 
# @File    : LeetCode235_最近公共组件.py
# @Software: PyCharm
# @desc    :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.res = root
        self.flag = False
        self.dfs(root, p, q)
        return self.res

    def dfs(self, node, p, q):
        if self.flag:
            return
        if not node:
            return
        if node == p:
            q_result = self.dfs(p.left, p, q) or self.dfs(p.right, p, q)
            if q_result:
                if self.flag:
                    return
                else:
                    self.res = node
                    self.flag = True
                    return
            return True
        if node == q:
            p_result = self.dfs(q.left, p, q) or self.dfs(q.right, p, q)
            if p_result:
                if self.flag:
                    return
                else:
                    self.res = node
                    self.flag = True
                    return
            return True
        p_result = self.dfs(node.left, p, q)
        q_result = self.dfs(node.right, p, q)
        if p_result and q_result:
            if self.flag:
                return
            else:
                self.res = node
                self.flag = True
                return
        return p_result or q_result


if __name__ == "__main__":
    solve = Solution()
    a = TreeNode(6)
    b = TreeNode(2)
    c = TreeNode(8)
    d = TreeNode(0)
    e = TreeNode(4)
    f = TreeNode(7)
    g = TreeNode(9)
    h = TreeNode(3)
    i = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i
    p = f
    q = g
    result = solve.lowestCommonAncestor(a, p, q)
    print(result.val)

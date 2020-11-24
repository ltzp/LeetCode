#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-24 18:18
# @Author  : Letao
# @Site    : 
# @File    : LeetCode222_安全二叉树的节点个数.py
# @Software: PyCharm
# @desc    :

import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root:
            return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(5)
    g = TreeNode(6)
    a.left = b
    a.right = c
    b.left = e
    b.right = f
    c.left = g
    solve = Solution()
    result = solve.countNodes(a)
    print(result)

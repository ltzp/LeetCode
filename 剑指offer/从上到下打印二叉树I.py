#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/04
# @Author  : yuetao
# @Site    : 
# @File    : 从上到下打印二叉树I.py
# @Desc    :



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        deque = collections.deque()
        deque.append(root)
        while deque:
            cur_node = deque.popleft()
            if cur_node.val not in res:
                res.append(cur_node.val)
            if cur_node.left:
                res.append(cur_node.left.val)
                deque.append(cur_node.left)
            if cur_node.right:
                res.append(cur_node.right.val)
                deque.append(cur_node.right)
        return res

if __name__ == '__main__':
    solve = Solution()
    a = TreeNode(3)
    b = TreeNode(9)
    d = TreeNode(20)
    e = TreeNode(15)
    f = TreeNode(7)
    a.left = b
    a.right = d
    d.left = e
    d.right = f
    result = solve.levelOrder(a)
    print(result)

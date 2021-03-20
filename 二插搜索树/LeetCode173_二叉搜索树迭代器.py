#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/20
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode173_二叉搜索树迭代器.py
# @Desc    :

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.deque = collections.deque()
        self.__order__mid(root)

    def __order__mid(self, root):
        if not root:
            return
        self.__order__mid(root.left)
        self.deque.append(root.val)
        self.__order__mid(root.right)



    def next(self):
        """
        :rtype: int
        """
        return self.deque.popleft()



    def hasNext(self):
        """
        :rtype: bool
        """
        if self.deque:
            return True
        return False


if __name__ == '__main__':
    root = TreeNode(7)
    a = TreeNode(3)
    b = TreeNode(15)
    c = TreeNode(9)
    d = TreeNode(20)
    root.left = a
    root.right = b
    c.left = c
    c.right = d
    bst = BSTIterator(root)
    print(bst.next())

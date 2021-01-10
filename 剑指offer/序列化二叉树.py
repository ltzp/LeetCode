#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/06
# @Author  : yuetao
# @Site    : 
# @File    : 序列化二叉树.py
# @Desc    :

import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return res
        queue = collections.deque()
        queue.append(root)
        lost_num_index = 0
        while queue:
            cur_node = queue.popleft()
            if not cur_node:
                res.append(cur_node)
                continue
            res.append(cur_node.val)
            lost_num_index = len(res)
            queue.append(cur_node.left)
            queue.append(cur_node.right)
        return res[:lost_num_index]


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = TreeNode(data.pop(0))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            left, right = None, None
            if data:
                item = data.pop(0)
                if item is not None:
                    left = TreeNode(item)
                    node.left = left
                    queue.append(left)
            if data:
                item = data.pop(0)
                if item is not None:
                    right = TreeNode(item)
                    node.right = right
                    queue.append(right)

        return root


if __name__ == '__main__':
    solve = Codec()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    result = solve.serialize(a)
    print(result)
    root = solve.deserialize(result)
    print(root)
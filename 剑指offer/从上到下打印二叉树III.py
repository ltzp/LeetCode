#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/06
# @Author  : yuetao
# @Site    : 
# @File    : 从上到下打印二叉树III.py
# @Desc    :
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = collections.deque()
        queue.append(root)
        row = 1
        while queue:
            size = len(queue)
            single_row = []
            while size > 0:
                cur_node = queue[0]
                queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                single_row.append(cur_node.val)
                size -= 1
            if row & 1:
                res.append(single_row)
            else:
                res.append(single_row[::-1])
            row += 1
        return res


if __name__ == '__main__':
    pass

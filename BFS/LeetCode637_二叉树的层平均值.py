#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 0013 14:34
# @Author  : Letao
# @Site    : 
# @File    : LeetCode637_二叉树的层平均值.py
# @Software: PyCharm
# @desc    :

import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        deque = collections.deque()

        level_dict = {root: 1}
        node_info = collections.defaultdict(list)
        deque.append(root)
        while deque:
            cur_node = deque.popleft()
            value = level_dict.get(cur_node)
            if cur_node.left:
                deque.append(cur_node.left)
                level_dict[cur_node.left] = value + 1
            if cur_node.right:
                deque.append(cur_node.right)
                level_dict[cur_node.right] = value + 1
        #print(level_dict)
        for key, value in level_dict.items():
            node_info[value].append(key.val)
        res = []
        for key, value in node_info.items():
            res.append(float(sum(value)/len(value)))
        return res

if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    solve = Solution()
    result = solve.averageOfLevels(a)
    print(result)
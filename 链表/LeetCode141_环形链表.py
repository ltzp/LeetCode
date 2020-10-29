#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 0009 21:32
# @Author  : Letao
# @Site    : 
# @File    : LeetCode141_环形链表.py
# @Software: PyCharm
# @desc    :

"""
快慢指针，龟兔算法
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        else:
            return True
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 0010 18:56
# @Author  : Letao
# @Site    : 
# @File    : LeetCode142_环形链表2.py
# @Software: PyCharm
# @desc    :


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        meet = None
        while(fast):
            slow = slow.next
            fast = fast.next
            if not fast:
                return
            fast = fast.next
            if fast == slow:
                meet = fast
                break
        if not meet:
            return
        while head and meet:
            if head == meet:
                return meet
            head = head.next
            meet = meet.next
        return

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/01/12
# @Author  : yuetao
# @Site    : 
# @File    : 两个链表的第一个公共节点.py
# @Desc    :

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node1, node2 = headA, headB
        while node1 != node2:
            if not node1:
                node1 = headB
            else:
                node1 = node1.next
            if not node2:
                node2 = headA
            else:
                node2 = node2.next
        return node1


if __name__ == '__main__':
    a = ListNode(4)
    b = ListNode(1)
    c = ListNode(8)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    a2 = ListNode(5)
    b2 = ListNode(0)
    c2 = ListNode(1)
    a2.next = b2
    b2.next = c2
    c2.next = c
    solve = Solution()
    result = solve.getIntersectionNode(a, a2)
    print(result.val)


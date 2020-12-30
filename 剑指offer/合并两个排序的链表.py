#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/30
# @Author  : yuetao
# @Site    : 
# @File    : 合并两个排序的链表.py
# @Desc    :

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1
        res = ListNode(None)
        p = res
        if l1.val <= l2.val:
            p.next = ListNode(l1.val)
            l1 = l1.next
            p = p.next
        else:
            p.next = ListNode(l2.val)
            l2 = l2.next
            p = p.next
        while l1 and l2:
            if p.val <= l1.val and l1.val < l2.val:
                p.next = ListNode(l1.val)
                p = p.next
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                p = p.next
                l2 = l2.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return res.next

if __name__ == '__main__':
    solve = Solution()
    a = ListNode(-10)
    b = ListNode(-10)
    c = ListNode(-9)
    d = ListNode(-4)
    e = ListNode(1)
    f = ListNode(6)
    g = ListNode(6)
    h = ListNode(-7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g


    result = solve.mergeTwoLists(a, h)
    while result:
        print(result.val)
        result = result.next


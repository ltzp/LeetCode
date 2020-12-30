#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/30
# @Author  : yuetao
# @Site    : 
# @File    : 反转链表.py
# @Desc    :

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        cur = head
        while cur:
            next = cur.next
            cur.next = new_head
            new_head = cur
            cur = next
        return new_head


if __name__ == '__main__':
    solve = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    result = solve.reverseList(a)
    while result:
        print(result.val)
        result = result.next


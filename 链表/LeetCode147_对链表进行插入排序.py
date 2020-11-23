#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-11-20 22:29
# @Author  : Letao
# @Site    : 
# @File    : LeetCode147_对链表进行插入排序.py
# @Software: PyCharm
# @desc    :

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        new_head = ListNode(None)
        new_head.next = head
        p,q, = new_head, new_head
        r = head
        while r:
            if not q.val:
                q = r
            elif r.val >= q.val:
                q.next = r
                q = r
            elif r.val < q.val:
                if r.val < p.next.val:
                    q.next = r.next
                    r.next = p.next
                    p.next = r
                else:
                    start = p.next
                    while start and start != q and start.next:
                        if r.val > start.val and  r.val < start.next.val:
                            break
                        start = start.next
                    q.next = r.next
                    r.next = start.next
                    start.next = r
            r = q.next
        return p.next



if __name__ == "__main__":
    solve = Solution()
    a = ListNode(1)
    b = ListNode(1)
    # c = ListNode(1)
    # d = ListNode(3)
    a.next = b
    # b.next = c
    # c.next = d
    result = solve.insertionSortList(a)
    while result:
        print(result.val)
        result = result.next

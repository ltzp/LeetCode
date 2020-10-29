#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 0013 17:54
# @Author  : Letao
# @Site    : 
# @File    : LeetCode24_两两交换链表中的结点.py
# @Software: PyCharm
# @desc    :

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        new_head = ListNode(None)
        new_head.next = head
        s = new_head
        p = new_head.next
        while p:
            if not p.next:
                break
            q = p.next
            r = q
            p.next = r.next
            q.next = p
            s.next = q
            s = p
            p = p.next
        return new_head.next




if __name__ == "__main__":
    solve = Solution()
    head = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    head.next = b
    b.next = c
    c.next = d
    d.next = e
    result = solve.swapPairs(head)
    while result:
        print(result.val)
        result = result.next

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/27
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode61_旋转链表.py
# @Desc    :

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        new_head = ListNode()
        new_head.next = head
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        if k%count == 0:
            return head
        remove_num = count - (k % count)
        q = head
        while remove_num > 1:
            remove_num -= 1
            q = q.next
        new_head.next = q.next
        q.next = None
        m = new_head.next
        while m:
            if not m.next:
                m.next = head
                break
            m = m.next
        return new_head.next


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
    k = 6
    result = solve.rotateRight(a, k)
    while result:
        print(result.val)
        result = result.next


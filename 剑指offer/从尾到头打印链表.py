#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 0013 20:47
# @Author  : Letao
# @Site    : 
# @File    : 从尾到头打印链表.py
# @Software: PyCharm
# @desc    : 链表反转

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        self.res = []
        pre = ListNode(None)
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        while pre:
            self.res.append(pre.val)
            pre = pre.next
        return self.res[:-1]


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(2)
    a.next = b
    b.next = c
    solve = Solution()
    result = solve.reversePrint(a)
    print(result)
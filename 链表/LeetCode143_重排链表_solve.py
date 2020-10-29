#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 0020 20:15
# @Author  : Letao
# @Site    : 
# @File    : LeetCode143_重排链表_solve.py
# @Software: PyCharm
# @desc    :

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        p = head
        node_arr = []
        while p:
            node_arr.append(p)
            p = p.next
        left, right = 0, len(node_arr)-1
        while left < right:
            node_arr[left].next = node_arr[right]
            left += 1
            if left == right:
                break
            node_arr[right].next = node_arr[left]
            right -= 1
        node_arr[left].next = None




if __name__ == "__main__":
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
    solve.reorderList(a)
    while a:
        print(a.val)
        a = a.next
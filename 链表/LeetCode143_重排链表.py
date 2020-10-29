#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 0020 18:14
# @Author  : Letao
# @Site    : 
# @File    : LeetCode143_重排链表.py
# @Software: PyCharm
# @desc    :

"""
在空间上O(1)
时间上0(N*N)
在同一个链表上操作，每次找到最后一个结点前一个结点，进行交换
"""

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
        length = 0
        while p:
            length += 1
            p = p.next
        new_head = head
        count = 0

        if length & 1:
            count = length//2
        else:
            count = length/2 - 1
        while new_head and count:
            index = 1
            pre_node = head
            while index < length - 1:
                pre_node = pre_node.next
                index += 1
            move_node = pre_node.next
            next_node = new_head.next
            new_head.next = move_node
            move_node.next = next_node
            pre_node.next = None
            new_head = move_node.next
            count -= 1
        return head


if __name__ == "__main__":
    solve = Solution()
    a = ListNode(1)
    # b = ListNode(2)
    # c = ListNode(3)
    # d = ListNode(4)
    # e = ListNode(5)
    # a.next = b
    # b.next = c
    # c.next = d
    # d.next = e
    result = solve.reorderList(a)
    while result:
        print(result.val)
        result = result.next
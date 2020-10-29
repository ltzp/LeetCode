#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 0023 22:11
# @Author  : Letao
# @Site    : 
# @File    : LeetCode234_回文链表.py
# @Software: PyCharm
# @desc    :


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        value = list()
        left_right = ""
        while head:
            value.append(head.val)
            left_right += str(head.val)
            head = head.next
        right_left = ""
        while value:
            right_left += str(value[-1])
            value.pop()
        if left_right == right_left:
            return True
        else:
            return False

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    solve = Solution()
    result = solve.isPalindrome(a)
    print(result)
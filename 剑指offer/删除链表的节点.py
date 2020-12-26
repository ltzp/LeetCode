#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/26
# @Author  : yuetao
# @Site    : 
# @File    : 删除链表的节点.py
# @Desc    :
"""
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

"""



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(None)
        new_head.next = head
        p = new_head
        while p:
            if p.next and p.next.val == val:
                q = p.next
                p.next = q.next
                break
            p = p.next
        return new_head.next



if __name__ == '__main__':
    solve = Solution()
    a = ListNode(4)
    b = ListNode(5)
    c = ListNode(1)
    d = ListNode(9)
    a.next = b
    b.next = c
    c.next = d
    val = 9
    result = solve.deleteNode(a, val)
    while result:
        print(result.val)
        result = result.next


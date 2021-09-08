#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/09/08
# @Author  : yuetao
# @Site    : 
# @File    : NC51_合并K个有序链表.py
# @Desc    :
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeKLists(self , lists ):
        new_head = None
        p = new_head
        head = []
        for i in range(len(lists)):
            while lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
        return new_head.next


if __name__ == '__main__':
    pass

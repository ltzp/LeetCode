#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/08
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode146_LRU缓存机制.py
# @Desc    :
import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.record_value = dict()
        self.max_length = capacity
        self.queue = collections.deque()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.record_value:
            return -1
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)
        return self.record_value.get(key)



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.record_value:
            # key在窗口中
            self.record_value[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            # key 不在窗口中
            if len(self.record_value) < self.max_length:
                #窗口还没有满
                self.record_value[key] = value
                self.queue.append(key)
            else:
                #窗口满了，该删除了
                remove_key = self.queue.popleft()
                self.record_value.pop(remove_key)
                self.record_value[key] = value
                self.queue.append(key)


if __name__ == '__main__':
    pass

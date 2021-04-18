#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/14
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode208_实现前缀树.py
# @Desc    :

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.isEnd = False


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self
        for c in word:
            index = ord(c) - ord("a")
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.isEnd = True

    def searchPrefix(self, prefix):
        node = self
        for c in prefix:
            index = ord(c) - ord("a")
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.searchPrefix(prefix) is not None


if __name__ == '__main__':
    pass

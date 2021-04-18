#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/18
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode211_添加与搜索单词 - 数据结构设计.py
# @Desc    :

class Node:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26


class WordDictionary(object):


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for s in word:
            index = ord(s) - ord('a')
            if cur.children[index] == None:
                cur.children[index] = Node()
            cur = cur.children[index]
        cur.isEnd = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.dfs(0, self.root, word)

    def dfs(self,index, node, word):
        if index == len(word):
            return node.isEnd
        cur_ch = word[index]
        if cur_ch == ".":
            for i in range(26):
                if node.children[i] and self.dfs(index+1, node.children[i], word):
                    return True
            return False
        else:
            if not node.children[ord(cur_ch) - ord('a')]:
                return False
            return self.dfs(index+1, node.children[ord(cur_ch) - ord('a')], word)



if __name__ == '__main__':
   word =  WordDictionary()
   word.addWord("bad")
   word.addWord("dad")
   word.addWord("mad")
   word.search("pad")
   word.search("bad")
   word.search(".ad")
   word.search("b..")


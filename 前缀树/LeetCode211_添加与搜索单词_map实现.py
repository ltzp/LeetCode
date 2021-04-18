#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/18
# @Author  : yuetao
# @Site    : 
# @File    : LeetCode211_添加与搜索单词_map实现.py
# @Desc    :
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/18
# @Author  : yuetao
# @Site    :
# @File    : LeetCode211_添加与搜索单词 - 数据结构设计.py
# @Desc    :
import collections
class Node:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(Node)


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
            cur = cur.children[s]
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
        cur_node = node
        cur_ch = word[index]
        if cur_ch == ".":
            for _node in cur_node.children.values():
                if self.dfs(index+1,_node , word):
                    return True
            return False
        else:
            cur_node = cur_node.children.get(cur_ch)
            if not cur_node:
                return False
            return self.dfs(index+1, cur_node, word)



if __name__ == '__main__':
   word =  WordDictionary()
   word.addWord("bad")
   word.addWord("dad")
   word.addWord("mad")
   word.search("pad")
   word.search("bad")
   word.search(".ad")
   word.search("b..")

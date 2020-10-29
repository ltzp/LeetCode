#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 0008 18:09
# @Author  : Letao
# @Site    : 
# @File    : LeetCode131.py
# @Software: PyCharm
# @desc    :


class Solution:
    def partition(self, s):
        n = len(s)
        self.result = []

        """
        回溯
        """
        def backtrack(s, begin, path):
            if begin == n:
                self.result.append(path[:])
                return
            for i in range(begin, n):
                if not isPlalindrome(s, begin, i):
                    continue
                path.append(s[begin:i + 1])
                backtrack(s, i + 1, path)
                path.pop()

        """
        判断是否回文
        """
        def isPlalindrome(s, left, right):
            if left > right:
                return False
            while left < right and left < n and right >= 0:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        backtrack(s, 0, [])
        return self.result


if __name__ == "__main__":
    solve = Solution()
    s = "aab"
    result = solve.partition(s)
    print(result)
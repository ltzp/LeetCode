#!/opt/anaconda3/bin/python
# -*- coding: UTF-8 -*-

# @Author : yuetao
# @File : LeetCode455_分发饼干.py
# @Time : 2020/12/25
# @Desc:

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child


if __name__ == '__main__':
    solve = Solution()
    g = [10,9,8,7]
    s = [5,6,7,8]
    result = solve.findContentChildren(g, s)
    print(result)
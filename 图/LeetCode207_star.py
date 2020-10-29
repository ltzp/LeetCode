#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 0004 18:58
# @Author  : Letao
# @Site    : 
# @File    : LeetCode207.py
# @Software: PyCharm
# @desc    : 图的广度遍历
# https://leetcode-cn.com/problems/course-schedule/
import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #存储有向图
        course_hash = collections.defaultdict(list)
        # 存储每个点的出入度
        indeg = [0] * numCourses
        result = 0
        for info in prerequisites:
            course_hash[info[1]].append(info[0])
            indeg[info[0]] += 1
        q = collections.deque()
        for u in range(numCourses):
            if indeg[u] == 0:
                q.append(u)
        while q:
            u = q.popleft()
            result += 1
            for v in course_hash[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return result == numCourses



if __name__ == "__main__":
    solve = Solution()
    numCourses = 3
    prerequisites = [[1,0],[0,2],[2,1]]
    result = solve.canFinish(numCourses, prerequisites)
    print(result)
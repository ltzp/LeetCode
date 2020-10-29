#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 0031 18:15
# @Author  : Letao
# @Site    : 
# @File    : LeetCode841.py
# @Software: PyCharm
# @desc    :

class Solution(object):

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms or len(rooms) == 1:
            return True
        length = len(rooms)
        self.opended_room = [False] * length
        self.dfs(rooms, [], 0)
        if False in self.opended_room:
            return False
        return True

    def dfs(self, rooms, use_key, cur_room):
        if self.opended_room[cur_room]:
            return
        if cur_room == 0:
            self.opended_room[0] = True
        if cur_room in use_key:
            self.opended_room[cur_room] = True
        contain_key = rooms[cur_room]
        #use_key = list(set(use_key + contain_key))
        for key in contain_key:
            if key not in use_key:
                use_key.append(key)
            self.dfs(rooms, use_key, key)


if __name__ == "__main__":
    solve = Solution()
    rooms = [[1,3],[3,0,1],[2],[0]]
    result = solve.canVisitAllRooms(rooms)
    print(result)
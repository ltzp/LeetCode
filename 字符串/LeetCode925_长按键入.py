#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 0021 18:05
# @Author  : Letao
# @Site    : 
# @File    : LeetCode925_长按键入.py
# @Software: PyCharm
# @desc    :


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        name_length = len(name)
        typed_length = len(typed)
        if typed_length < name_length:
            return False
        name_array = []
        i = 0
        while i < name_length:
            count = 1
            j = i + 1
            while j < name_length:
                if name[i] == name[j]:
                    count += 1
                    j += 1
                else:
                    break

            i = j

        # print(name_array)
        typed_array = []
        i = 0
        while i < typed_length:
            if typed[i] not in name:
                return False
            count = 1
            j = i + 1
            while j < typed_length:
                if typed[i] == typed[j]:
                    count += 1
                    j += 1
                else:
                    break
            i = j
            typed_array.append(count)
        # print(typed_array)
        if len(typed_array) != len(name_array):
            return False
        length = len(name_array)
        for i in range(length):
            if typed_array[i] < name_array[i]:
                return False
        return True



if __name__ == "__main__":
    solve = Solution()
    name = "laidez"
    typed = "laideccc"
    result = solve.isLongPressedName(name, typed)
    print(result)
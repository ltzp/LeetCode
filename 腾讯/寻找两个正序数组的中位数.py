#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/07
# @Author  : yuetao
# @Site    : 
# @File    : 寻找两个正序数组的中位数.py
# @Desc    :

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        index = 0
        other_flag = False
        if (m+n)&1:
            index = int((m+n)/2 + 1)
        else:
            other_flag = True
            index = int((m+n)/2)
        if m == 0 and n != 0:
            if not other_flag:#计数
                return nums2[index-1]
            else:
                return (nums2[index-1] + nums2[index])/2.0
        if m != 0 and n == 0:
            if not other_flag:#计数
                return nums1[index-1]
            else:
                return (nums1[index-1] + nums1[index])/2.0
        count, i, j = 0, 0, 0
        stack = []
        while count <= index:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    stack.append(nums1[i])
                    i += 1
                else:
                    stack.append(nums2[j])
                    j += 1
                count += 1
                continue
            elif i == m and j < n:
                stack.append(nums2[j])
                j += 1
                count += 1
                continue
            elif i < m and j == n :
                stack.append(nums1[i])
                i += 1
                count += 1
                continue
        if other_flag:
            return (stack[index] + stack[index-1])/2.0
        else:
            return stack[index-1]


if __name__ == '__main__':
    solve = Solution()
    nums1 = [0,0,0,0,0]

    nums2 = [-1,0,0,0,0,0,1]
    result = solve.findMedianSortedArrays(nums1, nums2)
    print(result)

"""
用HashMap 时间复杂度O(n)
空间复杂度O(N)
"""


import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 2:
            return list(set(nums))
        hash_map = dict()
        counter = math.ceil(len(nums)/3)
        res = []
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        for key,value in hash_map.items():
            if value > counter:
                res.append(key)
        return res


if __name__ == "__main__":
    solve = Solution()
    nums = []
    result = solve.majorityElement(nums)
    print(result)
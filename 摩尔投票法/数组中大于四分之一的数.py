import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        if not len(nums):
            return res
        cant1, cant2, cant3 = nums[0], nums[0], nums[0]
        count1, count2, count3 = 0, 0, 0
        for num in nums:
            if cant1 == num:
                count1 += 1
                continue
            if cant2 == num:
                count2 += 1
                continue
            if cant3 == num:
                count3 += 1
            if not count1:
                cant1 = num
                count1 = 1
                continue
            if not count2:
                cant2 = num
                count2 = 1
                continue
            if not count3:
                cant3 = num
                count3 = 1
            count1 -= 1
            count2 -= 1
            count3 -= 1
        count1, count2, count3 = 0, 0, 0
        for i in nums:
            if i == cant1:
                count1 += 1
            elif i == cant2:
                count2 += 1
            elif i == cant3:
                count3 += 1
        if count1 > len(nums)/4:
            res.append(cant1)
        if count2 > len(nums)/4:
            res.append(cant2)
        if count3 > len(nums)/4:
            res.append(cant3)
        return res



if __name__ == "__main__":
    solve = Solution()
    nums = [1,3,3,4,3,5,]
    result = solve.majorityElement(nums)
    print(result)
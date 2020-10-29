class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        cur_num = nums[0]
        for num in nums:
            if count == 0:
                count += 1
                cur_num = num
            else:
                if num == cur_num:
                    count += 1
                else:
                    count -= 1
        return cur_num


if __name__ == "__main__":
    solve = Solution()
    nums = [6,5,5]
    result = solve.majorityElement(nums)
    print(result)
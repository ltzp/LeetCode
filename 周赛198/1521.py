"""
解题思路:排序-去重
1.arr所有数去重，因为只要自身与自身与一次即可，在多次还是自身
2.内层循环第一次与的结果比目标值相等或是小时，跳出该循环，再往后与会越小，距离目标值就越远

"""


class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr = sorted(list(set(arr)), key=arr.index)
        res = float('inf')
        for i in range(0, len(arr)):
            ans = arr[i]
            for j in range(i, len(arr)):
                ans &= arr[j]
                res = min(res, abs(ans - target))
                if ans <= target:
                    break
        return res


if __name__ == "__main__":
    solve = Solution()
    arr = [9, 12, 3, 7, 15]
    target = 5
    result = solve.closestToTarget(arr, target)
    print(result)
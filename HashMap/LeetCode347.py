"""
基数排序、桶排序和计数排序的区别
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = dict()
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        print(hash)
        n = len(nums)
        s = [0]*(n+1)
        for key, valus in hash.items():
            s[valus] = s[valus] +1
        i, t = n, 0
        while t < k:
            t += s[i]
            i = i - 1
        res = []
        for key, valus in hash.items():
            if valus > i:
                res.append(key)
        return res

if __name__=="__main__":
    solve = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    result = solve.topKFrequent(nums, k)
    print(result)
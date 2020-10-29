"""
测试用例:986 / 987 个通过测试用例

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        length = len(s)
        if length <= 1:
            return length
        node = length
        while node > 0:
            i = 0
            while i + node <= length:
                str = s[i: i+ node]
                hash_map = dict()
                for k in str:
                    if k not in hash_map:
                        hash_map[k] = 1
                    else:
                        break
                if len(hash_map) == node:
                    res = node
                    return res
                i += 1
            node -= 1
        return res


if __name__ == "__main__":
    solve = Solution()
    s = "bbbbb"
    result = solve.lengthOfLongestSubstring(s)
    print(result)
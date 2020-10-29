class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n = len(s)
        my_strs = [""]*n
        for i in range(0, n):
            str = s[i]
            my_strs[indices[i]] = str
        result = ""
        for my_str in my_strs:
            result += my_str
        return result


if __name__=="__main__":
    solve = Solution()
    s = "aiohn"
    indices = [3, 1, 4, 2, 0]
    result = solve.restoreString(s, indices)
    print(result)
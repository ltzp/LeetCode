

class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        str_index = {}
        for i in range(0, len(s)):
            if str_index.get(s[i]):
                str_index[s[i]][1] = i
            else:
                str_index[s[i]] = [i, i]
        ans = []
        for start, end in str_index.values():
            i = start + 1
            maxend = end
            while i < maxend:
                if str_index[s[i]][0] < start:
                    break
                maxend =max(maxend, str_index[s[i]][1])
                i += 1
            else:
                ans.append([start, end])
        res = []
        for p in ans:
            for q in ans:
                if p!=q and p[0] <= q[0] and p[1]>=q[1]:
                    break
            else:
                res.append(s[p[0]:p[1]+1])
        return res


if __name__ == "__main__":
    solve = Solution()
    s = "adefaddaccc"
    result = solve.maxNumOfSubstrings(s)
    for i in result:
        print(i)

"""
桶计数法
"""

class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0] * 26
        for i in s:
            count[ord(i) - 97] += 1
        print(count)
        res = ''
        flag = 1
        while len(res) != len(s):
            if flag == 1:
                for i in range(len(count)):
                    if count[i] != 0:
                        res += chr(97+i)
                        count[i] -= 1
                flag = -1
            if flag == -1:
                length = len(count)
                while length:
                    if count[length-1] != 0:
                        res += chr(97+length-1)
                        count[length-1] -= 1
                    length -= 1
                flag = 1
        return res



if __name__ == "__main__":
    solve = Solution()
    s = "aaaabbbbcccc"
    result = solve.sortString(s)
    print(result)
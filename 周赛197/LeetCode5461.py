"""
输入：s = "0110111"
输出：9
解释：共有 9 个子字符串仅由 '1' 组成
"1" -> 5 次
"11" -> 3 次
"111" -> 1 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-substrings-with-only-1s
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        if len(s) == 0:
            return result
        # 进行按0拆分
        nums = s.split('0')
        for i in nums:
            result = result + (len(i) + 1) * len(i) / 2;
            result = result % 1000000007
        return result

if __name__=="__main__":
     solve = Solution()
     s = "0110111"
     result = solve.numSub(s)
     print(result)



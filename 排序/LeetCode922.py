class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        C = []
        for a in A:
            if a%2 == 0:
                B.append(a)
            else:
                C.append(a)
        res = []
        for i in range(len(B)):
            res.append(B[i])
            res.append(C[i])
        return res


if __name__=="__main__":
    solve = Solution()
    A = [4,2,5,7]
    result = solve.sortArrayByParityII(A)
    print(result)
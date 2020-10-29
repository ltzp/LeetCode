class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        length = len(arr)
        res = 0
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        print(arr[i], arr[j], arr[k])
                        res += 1
        return res

if __name__=="__main__":
    solve = Solution()
    arr = [1,1,2,2,3]
    a = 0
    b = 0
    c = 1
    result = solve.countGoodTriplets(arr, a, b, c)
    print(result)
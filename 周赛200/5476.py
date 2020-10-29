import collections

class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        flag = arr[0]
        #length = len(arr)
        best_max = max(arr)
        count = 0
        while True:
            if arr[0] <arr[1]:
                flag = arr[1]
                count = 1
                arr.append(arr[0])
                del arr[0]
            else:
                count+=1
                arr.append(arr[1])
                del arr[1]
            if count == k:
                return flag
            elif flag == best_max:
                return flag




if __name__ == "__main__":
    solve = Solution()
    arr = [282,788,890,547,60,322,263,843,392,837,822,452,830,417,179]
    k = 1
    res = solve.getWinner(arr, k)
    print(res)
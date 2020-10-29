import math

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        hash_map = dict()
        res = 0
        for number in numbers:
            if number not in hash_map:
                hash_map[number] = 1
            else:
                hash_map[number] += 1
        if length%2 == 0:
            count_max = length/2 + 1
        else:
            count_max = math.ceil(length / 2.0)

        print(count_max)
        for key, value in hash_map.items():
            if value >= count_max:
                res = key
                break
        return res




if __name__ == "__main__":
    solve = Solution()
    numbers = [4,2,1,4,2,4]
    result = solve.MoreThanHalfNum_Solution(numbers)
    print(result)
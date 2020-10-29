import math

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        result = numBottles
        null_bootle = numBottles
        if numExchange > numBottles:
            return numBottles
        while null_bootle >= numExchange:
            exchange_bootle = math.floor(null_bootle / numExchange)
            result = result + exchange_bootle
            rev = null_bootle - exchange_bootle*numExchange
            null_bootle = rev + exchange_bootle
        return result


if __name__ == "__main__":
    solve = Solution()
    numBottles = 5
    numExchange = 5
    result = solve.numWaterBottles(numBottles, numExchange)
    print(result)

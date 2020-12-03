class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            buy = min(buy, price)
            profit = max(price - buy, profit)
        return profit


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 6 - 1, "First"
    assert s.maxProfit([2, 7, 9, 3, 1]) == 7, "Second"
    assert s.maxProfit([2, 1, 1, 2]) == 1, "Third"
    assert s.maxProfit([2, 6, 4, 6, 1, 4]) == 4, "Fifth"
    assert s.maxProfit([2, 3, 2]) == 1, "Sixes"
    assert s.maxProfit([8, 2, 8, 9, 2]) == 7, "Seventh"
    assert s.maxProfit([7, 6, 5, 4, 3, 2, 1]) == 0, "Eight"

    print("PASSED!!!")

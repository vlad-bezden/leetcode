"""122. Best Time to Buy and Sell Stock II.

Level: Medium

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


class Solution:
    @staticmethod
    def maxProfit(prices: list[int]) -> int:
        """
        For each daily price check if today price is higher than previous
        price, then add difference to the profit
        """
        profit = 0
        prev_price = prices[0]
        for p in prices[1:]:
            if p > prev_price:
                profit += p - prev_price
            prev_price = p
        return profit


if __name__ == "__main__":
    tests = (([7, 1, 5, 3, 6, 4], 7), ([1, 2, 3, 4, 5], 4), ([7, 6, 4, 3, 1], 0))
    for test in tests:
        input, expected = test
        output = Solution.maxProfit(input)
        assert output == expected, f"{input = }, {output = }, {expected = }"

    print("PASSED!!!")

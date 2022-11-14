"""279. Perfect Squares.

Level: Medium

https://leetcode.com/problems/perfect-squares/
"""


class Solution:
    @staticmethod
    def numSquares(n: int) -> int:
        dp = [0]
        while len(dp) <= n:
            dp += (min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,)
        return dp[n]


if __name__ == "__main__":
    tests = ((12, 3), (13, 2), (8405, 2))
    for test in tests:
        input, expected = test
        result = Solution.numSquares(input)
        assert result == expected, f"{input=}, {result=}, {expected=}"

    print("PASSED!!!")

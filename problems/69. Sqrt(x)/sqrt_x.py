"""69. Sqrt(x)

Level: Easy

https://leetcode.com/problems/sqrtx/
"""

import math


class Solution:
    @staticmethod
    def mySqrt(x: int) -> int:
        if x < 2:
            return x
        lp, rp = 0, x // 2
        answer = 0

        while lp <= rp:
            mid = (lp + rp) // 2
            if (mid * mid) <= x:
                answer = mid
                lp = mid + 1
            else:
                rp = mid - 1
        return answer


if __name__ == "__main__":
    for i in range(100):
        expected = math.floor(math.sqrt(i))
        result = Solution.mySqrt(i)
        assert result == expected, print(f"{i =}, {result = }, {expected = }")

    print("PASSED!!!")

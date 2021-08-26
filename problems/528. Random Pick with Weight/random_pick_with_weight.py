"""528. Random Pick with Weight.

https://leetcode.com/problems/random-pick-with-weight/
"""

from random import randrange
from bisect import bisect_left


class Solution:
    def __init__(self, w: list[int]) -> None:
        prefix_sums = []
        total_sum = 0
        for val in w:
            total_sum += val
            prefix_sums.append(total_sum)
        self.prefix_sums = prefix_sums

    def pickIndex(self) -> int:
        prefix_sums = self.prefix_sums
        value = randrange(1, prefix_sums[-1] + 1)
        return bisect_left(prefix_sums, value)


if __name__ == "__main__":
    solution = Solution([1])
    assert solution.pickIndex() == 0
    input = [1, 3]
    solution = Solution(input)
    output = [solution.pickIndex() for _ in range(5)]
    expected = [1, 1, 1, 1, 0]
    assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

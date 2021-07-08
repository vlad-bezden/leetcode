"""238. Product of Array Except Self"""


from itertools import accumulate
from operator import mul


class Solution:
    @staticmethod
    def productExceptSelf(nums: list[int]) -> list[int]:
        left = [1] + [*accumulate(nums[:-1], mul)]
        right = [*reversed([*accumulate(nums[len(nums) : 0: -1], mul)])] + [1]
        return [mul(*i) for i in zip(left, right)]


if __name__ == "__main__":
    inputs = (
        ([5, 10, 15, 20, 25, 2], [150000, 75000, 50000, 37500, 30000, 375000]),
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([10, 20], [20, 10]),
    )
    for input, expected in inputs:
        output = Solution.productExceptSelf(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

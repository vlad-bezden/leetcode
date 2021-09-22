"""485. Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/
"""

from itertools import groupby


class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: list[int]) -> int:
        """Use itertools.groupby function."""
        return max((sum(g) for k, g in groupby(nums) if k), default=0)

    def findMaxConsecutiveOnes_2(nums: list[int]) -> int:
        """Inplace count 1s, update list values and find max value."""
        for i, v in enumerate(nums[1:], start=1):
            nums[i] = v * (v + nums[i - 1])
        return max(nums)


inputs = (([0], 0), ([1, 1, 0, 1, 1, 1], 3), ([1], 1), ([1, 1, 1], 3))

for input, expected in inputs:
    output = Solution.findMaxConsecutiveOnes(input)
    assert output == expected, f"{input=}, {output=}, {expected=}"
    output = Solution.findMaxConsecutiveOnes_2(input)
    assert output == expected, f"{input=}, {output=}, {expected=}"

print("PASSED!!!")

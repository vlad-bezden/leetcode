"""2104. Sum of Subarray Ranges.

Level: Medium

Brute force solution:
    O(n^2) time complexity
    O(1) space complexity

https://leetcode.com/problems/sum-of-subarray-ranges/
"""


class Solution:
    @staticmethod
    def subArrayRanges(nums: list[int]) -> int:
        result = 0

        for i, lv in enumerate(nums):
            min_ = max_ = lv

            for rv in nums[i + 1 :]:
                min_ = min(min_, rv)
                max_ = max(max_, rv)
                result += max_ - min_

        return result

"""215. Kth Largest Element in an Array

https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from heapq import nlargest


class Solution:
    @staticmethod
    def findKthLargest(nums: list[int], k: int) -> int:
        return nlargest(k, nums)[-1]


if __name__ == "__main__":
    inputs = (
        (([3, 2, 1, 5, 6, 4], 2), 5),
        (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
    )
    for input, expected in inputs:
        output = Solution.findKthLargest(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

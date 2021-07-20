"""Shuffle an Array.

    https://leetcode.com/problems/shuffle-an-array/
"""
from random import sample


class Solution:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        self.len = len(nums)

    def reset(self) -> list[int]:
        """Resets the array to its original configuration and return it."""
        return self.nums

    def shuffle(self) -> list[int]:
        """Returns a random shuffling of the array."""
        return sample(self.nums, self.len)


if __name__ in "__main__":
    input = sample(range(100), 20)
    print(input)
    solution = Solution(input)
    shuffle = solution.shuffle()
    assert set(solution.shuffle()) == set(input), "Invalid shuffle."
    assert solution.reset() == input, "Invalid reset"

    print("PASSED!!!")

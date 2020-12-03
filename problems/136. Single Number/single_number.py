class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)

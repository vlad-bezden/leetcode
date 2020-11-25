class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        vals = [0] * len(nums)
        for i, x in enumerate(nums):
            vals[i] = x + max(vals[: i - 1] or [0])
        return max(vals)


if __name__ == "__main__":
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == sum([1, 3]), "First"
    assert s.rob([2, 7, 9, 3, 1]) == sum([2, 9, 1]), "Second"
    assert s.rob([2, 1, 1, 2]) == sum([2, 2]), "Third"
    assert s.rob([1, 6, 4, 6, 2, 5, 4, 1, 4, 2]) == sum([6, 6, 5, 4]), "Fifth"
    assert s.rob([2, 3, 2]) == sum([2, 2]), "Six"
    assert s.rob([8, 2, 8, 9, 2]) == sum([8, 8, 2])

    print("PASSED!!!")

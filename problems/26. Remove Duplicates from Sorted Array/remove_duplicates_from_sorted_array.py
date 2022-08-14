"""26. Remove Duplicates from Sorted Array.

Level: Easy

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

# Valid values are -100 <= nums[i] <= 100
# any number outside of that range will be no value
nan = 2**10


class Solution:
    @staticmethod
    def removeDuplicates(nums: list[int]) -> int:
        p = 0
        for v in nums[1:]:
            if nums[p] != v:
                p += 1
                nums[p] = v
        return p + 1


if __name__ == "__main__":
    tests = (
        ([1, 2], 2),
        ([1], 1),
        (
            [1, 1, 2],
            2,
        ),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    )
    for test in tests:
        input, expected = test
        output = Solution.removeDuplicates(input)
        assert output == expected, f"{input =}, {output =}, {expected =}"

    print("PASSED!!!")

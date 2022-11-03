"""46. Permutations.

Level: Medium

https://leetcode.com/problems/permutations/
"""


class Solution:
    @staticmethod
    def permute(nums: list[int]) -> list[list[int]]:
        permutations = []
        nums_len = len(nums)

        def _permute(first: int = 0) -> None:
            if first == nums_len:
                permutations.append(nums.copy())
                return  # not required, but more readable
            for i in range(first, nums_len):
                nums[first], nums[i] = nums[i], nums[first]
                _permute(first + 1)
                # backtrack (reverse to previous values)
                nums[first], nums[i] = nums[i], nums[first]

        _permute()
        return permutations


if __name__ == "__main__":
    tests = (
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    )
    for test in tests:
        input, expected = test
        output = Solution.permute(input)
        output_set = set(map(tuple, output))
        assert not (
            output_set.symmetric_difference(map(tuple, expected))
        ), f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

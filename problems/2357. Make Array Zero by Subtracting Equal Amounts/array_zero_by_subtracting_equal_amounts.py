"""2357. Make Array Zero by Subtracting Equal Amounts

Level: Easy

https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
"""


class Solution:
    @staticmethod
    def minimumOperations(nums: list[int]) -> int:
        return len(set(nums) - {0})


if __name__ == "__main__":
    tests = (([1, 5, 0, 3, 5], 3), ([0], 0))
    for test in tests:
        input, expected = test
        result = Solution.minimumOperations(input)
        assert result == expected, f"{input=}, {result=}, {expected=}"

    print("PASSED!!!")

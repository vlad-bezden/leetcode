"""560. Subarray Sum Equals K

    https://leetcode.com/problems/subarray-sum-equals-k/
"""


class Solution:
    @staticmethod
    def subarraySum(nums: list[int], k: int) -> int:
        sums_count = {0: 1}
        counter = 0
        nums_sum = 0
        for n in nums:
            nums_sum += n
            counter += sums_count.setdefault(nums_sum - k, 0)
            sums_count[nums_sum] = sums_count.setdefault(nums_sum, 0) + 1
        return counter


if __name__ == "__main__":
    inputs = (
        (([1, 1, 1], 2), 2),
        (([1, 2, 3], 3), 2),
        (([0], 0), 1),
        (([1, 3, 1, 4, 4, 2, 1, 1, 2], 4), 6),
        (([1, -1, 1, -1, 1, -1], 0), 9),
        (([3, 4, 7, 2, -3, 1, 4, 2], 7), 4),
    )

    for input, expected in inputs:
        output = Solution.subarraySum(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

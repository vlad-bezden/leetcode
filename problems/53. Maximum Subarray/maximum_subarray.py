"""53. Maximum Subarray Solution

    Check if number is bigger than current sum than reset
    all counter and start to count from beggining.
    For all other cases accumulate new sum and
"""


class Solution:
    @staticmethod
    def maxSubArray(nums: list[int]) -> int:
        current_max = total_max = nums[0]
        for n in nums[1:]:
            current_max = max(n, current_max + n)
            total_max = max(total_max, current_max)
        return total_max


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == sum([4, -1, 2, 1])
    assert s.maxSubArray([1]) == sum([1])
    assert s.maxSubArray([0]) == sum([0])
    assert s.maxSubArray([-1]) == sum([-1])
    assert s.maxSubArray([-2147483647]) == sum([-2147483647])
    assert s.maxSubArray([-1, -2]) == sum([-1])

    print("PASSED!!!")

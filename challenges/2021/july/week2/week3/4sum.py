"""4Sum

    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3816/
"""


class Solution:
    @staticmethod
    def fourSum(nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        answer = set()
        end_idx = len(nums) - 1
        for i1, v1 in enumerate(nums):
            for i2, v2 in enumerate(nums[i1 + 1 :], start=i1 + 1):
                goal = target - v1 - v2
                start = i2 + 1
                end = end_idx
                while start < end:
                    start_val, end_val = nums[start], nums[end]
                    if start_val + end_val < goal:
                        start += 1
                    elif start_val + end_val > goal:
                        end -= 1
                    else:
                        answer.add((v1, v2, start_val, end_val))
                        start += 1
                        end -= 1
        return answer


if __name__ == "__main__":
    inputs = (
        (([1, 0, -1, 0, -2, 2], 0), {(-2, -1, 1, 2), (-1, 0, 0, 1), (-2, 0, 0, 2)}),
        (([2, 2, 2, 2, 2, 2], 8), {(2, 2, 2, 2)}),
        (([0, 0, 0, 0], 0), {(0, 0, 0, 0)}),
        (([-1, 0, 1, 2, -1, -4], -1), {(-4, 0, 1, 2), (-1, -1, 0, 1)}),
        (([1, -2, -5, -4, -3, 3, 3, 5], -11), {(-5, -4, -3, 1)}),
    )
    for input, expected in inputs:
        output = Solution.fourSum(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

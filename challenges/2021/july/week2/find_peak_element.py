"""Find Peak Element

    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3812/
"""


class Solution:
    @staticmethod
    def findPeakElement(nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    inputs = (
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5),  # 2 is accaptable answer too
    )
    for input, expected in inputs:
        output = Solution.findPeakElement(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

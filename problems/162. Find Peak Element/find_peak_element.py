"""162. Find Peak Element"""


class Solution:
    @staticmethod
    def findPeakElement(nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[middle + 1]:
                right = middle
            else:
                left = middle + 1
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

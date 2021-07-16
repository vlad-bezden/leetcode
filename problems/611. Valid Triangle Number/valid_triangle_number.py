"""611. Valid Triangle Number"""


class Solution:
    @staticmethod
    def triangleNumber(nums: list[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums) - 1, 1, -1):
            anchor = nums[i]
            right = i - 1
            left = 0
            while left < right:
                if nums[right] + nums[left] > anchor:
                    result += right - left
                    right -= 1
                else:
                    left += 1
        return result


if __name__ == "__main__":
    inputs = (([2, 2, 3, 4], 3), ([4, 2, 3, 4], 4))

    for input, expected in inputs:
        output = Solution.triangleNumber(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

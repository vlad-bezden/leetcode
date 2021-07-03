class Solution:
    @staticmethod
    def maximumProduct(nums: list[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


if __name__ == "__main__":
    inputs = [
        [[1, 2, 3], 6],
        [[1, 2, 3, 4], 24],
        [[-1, -2, -3], -6],
        [[-20, -50, 1, 2, 3], 3000],
    ]

    s = Solution()
    for input, expected in inputs:
        output = s.maximumProduct(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

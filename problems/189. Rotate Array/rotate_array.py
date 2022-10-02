"""189. Rotate Array.

Level: Medium

https://leetcode.com/problems/rotate-array/
"""


class Solution:
    @staticmethod
    def rotate(nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # option 1
        length = len(nums)
        k = k % length
        nums[:k], nums[k:] = nums[-k:], nums[: length - k]

        # option 2. This one is faster on LL
        # l = len(nums)
        # k = k % l
        # tail = nums[-k:]
        # for i in range(l - k):
        #     nums[-i - 1] = nums[-k - 1 - i]
        # for i, v in enumerate(tail):
        #     nums[i] = v


if __name__ == "__main__":
    tests = (
        (([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]),
        (([-1, -100, 3, 99], 2), [3, 99, -1, -100]),
    )
    for test in tests:
        input, expected = test
        Solution.rotate(*input)
        assert input[0] == expected, f"{input[0] = }, {expected = }"

    print("PASSED!!!")

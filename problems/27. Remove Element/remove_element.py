"""27. Remove Element

Level: Easy

https://leetcode.com/problems/remove-element/
"""


class Solution:
    @staticmethod
    def removeElement(nums: list[int], val: int) -> int:
        index = 0
        for n in nums:
            if n != val:
                nums[index] = n
                index += 1
        return index


if __name__ == "__main__":
    tests = (
        (([3, 2, 2, 3], 3), [2, 2]),
        (([3, 3, 2, 3], 3), [2]),
        (([0, 1, 2, 2, 3, 0, 4, 2], 2), [0, 1, 3, 0, 4]),
    )
    for test in tests:
        input, expected = test
        result = Solution.removeElement(*input)
        values = input[0][:result]
        assert values == expected, f"{values = }, {expected = }"

    print("PASSED!!!")

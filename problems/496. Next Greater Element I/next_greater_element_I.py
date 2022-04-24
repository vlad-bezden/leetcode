"""496. Next Greater Element I.

Level: Easy

https://leetcode.com/problems/next-greater-element-i/
"""


class Solution:
    @staticmethod
    def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        hash_map = {}

        for num in nums2:
            while stack and stack[-1] < num:
                hash_map[stack.pop()] = num
            stack.append(num)

        return [hash_map.get(i, -1) for i in nums1]


if __name__ == "__main__":
    tests = (
        (([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1]),
        (([2, 4], [1, 2, 3, 4]), [3, -1]),
    )
    for test in tests:
        input, expected = test
        result = Solution.nextGreaterElement(*input)
        assert result == expected

    print("PASSED!!!")

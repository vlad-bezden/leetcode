"""344. Reverse String.

Level: Easy

https://leetcode.com/problems/reverse-string/
"""


class Solution:
    @staticmethod
    def reverseString(string: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left_idx, right_idx = 0, len(string) - 1

        while left_idx < right_idx:
            string[left_idx], string[right_idx] = string[right_idx], string[left_idx]
            left_idx += 1
            right_idx -= 1


if __name__ == "__main__":
    tests = (
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    )

    for test in tests:
        input, expected = test
        Solution.reverseString(input)
        assert input == expected

    print("PASSED!!!")

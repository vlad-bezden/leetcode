"""541. Reverse String II.

Level: Easy

https://leetcode.com/problems/reverse-string-ii/
"""


class Solution:
    @staticmethod
    def reverseStr(string: str, k: int) -> str:
        result = list(string)
        for i in range(0, len(string), 2 * k):
            result[i : i + k] = reversed(result[i : i + k])

        return "".join(result)


if __name__ == "__main__":
    tests = (
        (("abcdefg", 2), "bacdfeg"),
        (("abcd", 2), "bacd"),
        (("abcdefg", 8), "gfedcba"),
    )

    for test in tests:
        input, expected = test
        result = Solution.reverseStr(*input)
        assert result == expected

    print("PASSED!!!")

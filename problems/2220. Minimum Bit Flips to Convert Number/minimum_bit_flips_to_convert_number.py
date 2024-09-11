"""2220. Minimum Bit Flips to Convert Number.

Level: Easy

https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
"""


class Solution:
    @staticmethod
    def minBitFlips(start: int, goal: int) -> int:
        return (bin(start ^ goal)).count("1")


if __name__ == "__main__":
    tests = (((10, 7), 3), ((3, 4), 3))
    for test in tests:
        input, expected = test
        output = Solution.minBitFlips(*input)
        assert output == expected, f"{input = }, {output = }, {expected = }"

    print("PASSED!!!")

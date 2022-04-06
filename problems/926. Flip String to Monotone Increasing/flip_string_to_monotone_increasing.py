"""926. Flip String to Monotone Increasing.

https://leetcode.com/problems/flip-string-to-monotone-increasing/
"""


class Solution:
    @staticmethod
    def minFlipsMonoIncr(string: str) -> int:
        result = 0
        seen_ones = 0
        for c in string:
            if c == "0":
                result = min(
                    result + 1,  # flip this '0' to '1'
                    seen_ones,  # flip all '1' we've seen before to '0'
                )
            else:
                seen_ones += 1
        return result


if __name__ == "__main__":
    tests = (
        ("00000", 0),
        ("11111", 0),
        ("00110", 1),  # 00111
        ("010110", 2),  # 011111 or 000111
        ("00011000", 2),  # 00000000
        ("0010011", 1),  # 0000011
    )

    for test in tests:
        input, expected = test
        result = Solution.minFlipsMonoIncr(input)
        assert result == expected

    print("PASSED!!!")

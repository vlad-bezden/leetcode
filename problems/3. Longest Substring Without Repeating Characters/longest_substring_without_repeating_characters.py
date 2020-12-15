"""Longest Substring Without Repeating Characters.

    Second method (using dict) to keep track of the current processing
    string is about 1.5-3 times slower.
"""
from timeit import timeit


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Using list of chars to keep current substring."""
        str_list = []
        answer = 0

        for c in s:
            if c in str_list:
                str_list = str_list[str_list.index(c) + 1 :]
            str_list.append(c)
            answer = max(answer, len(str_list))

        return answer

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        """Using dict for keeping track of latest position of chars."""
        # mp stores the current index of a character
        hm = {}
        max_length = 0
        start_index = 0

        for i, c in enumerate(s, start=1):
            if c in hm:
                start_index = max(hm[c], start_index)
            max_length = max(max_length, i - start_index)
            hm[c] = i

        return max_length


if __name__ == "__main__":
    solution = Solution()
    inputs = ["abba", "abcabcbb", "bbbbb", "pwwkew", "aab", "dvdf", " ", ""]
    expected = [
        len("ab"),
        len("abc"),
        len("b"),
        len("wke"),
        len("ab"),
        len("vdf"),
        1,
        0,
    ]

    funcs = [
        solution.lengthOfLongestSubstring,
        solution.lengthOfLongestSubstring_2,
    ]
    for f, input, expect in (
        (f, i, e) for i, e in zip(inputs, expected) for f in funcs
    ):
        print(f"\nRunning {f.__name__}")
        for input, expect in zip(inputs, expected):
            output = f(input)
            assert output == expect, f"{input=}, {expect=}, {output=}"
            t = timeit(
                stmt=f"f('{input}')",
                number=10_000,
                globals=globals(),
            )
            print(f"{f.__name__} took: {t:.6f}")

    print("PASSED!!!")

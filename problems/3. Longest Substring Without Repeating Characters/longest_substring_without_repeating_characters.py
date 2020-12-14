"""Longest Substring Without Repeating Characters."""
from timeit import timeit


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        current_longest = ""

        for c in s:
            if c in current_longest:
                answer = max(len(current_longest), answer)
                current_longest = c
            else:
                current_longest += c

        return answer

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        answer = 0
        current_map = set()

        for c in s:
            if c in current_map:
                answer = max(len(current_map), answer)
                current_map = set(c)
            else:
                current_map.add(c)

        return answer

    def lengthOfLongestSubstring_3(self, s: str) -> int:
        n = len(s)
        answer = 0
        # mp stores the current index of a character
        current_map = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in current_map:
                i = max(current_map[s[j]], i)

            answer = max(answer, j - i + 1)
            current_map[s[j]] = j + 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    inputs = ["abcabcbb", "bbbbb", "pwwkew"]
    expected = [len("abc"), len("b"), len("wke")]

    funcs = [
        solution.lengthOfLongestSubstring,
        solution.lengthOfLongestSubstring_2,
        solution.lengthOfLongestSubstring_3,
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

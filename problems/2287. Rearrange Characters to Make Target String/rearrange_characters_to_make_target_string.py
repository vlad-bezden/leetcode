"""2287. Rearrange Characters to Make Target String.

Level: Easy

https://leetcode.com/problems/rearrange-characters-to-make-target-string/
"""


from collections import Counter


class Solution:
    @staticmethod
    def rearrangeCharacters(s: str, target: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(target)
        return min(s_counter[k] // v for k, v in t_counter.items())


if __name__ == "__main__":
    tests = (
        (("ilovecodingonleetcode", "code"), 2),
        (("abcba", "abc"), 1),
        (("abbaccaddaeea", "aaaaa"), 1),
    )
    for test in tests:
        input, expected = test
        output = Solution.rearrangeCharacters(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

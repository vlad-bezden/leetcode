"""28. Find the Index of the First Occurrence in a String

Level: Easy

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
"""


class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)

        if h < n:
            return -1

        i = j = 0

        while i < h:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == n:
                    return i - n
            else:
                i = i - j + 1
                j = 0

        return -1


if __name__ == "__main__":
    tests = (
        (("sadbutsad", "sad"), 0),
        (("leetcode", "leeto"), -1),
        (("a", "a"), 0),
        (("abc", "c"), 2),
    )
    for test in tests:
        inputs, expected = test
        output = Solution.strStr(*inputs)
        assert output == expected, f"{inputs = }, {output = }, {expected = }"

    print("PASSED!!!")

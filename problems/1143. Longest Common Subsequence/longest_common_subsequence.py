"""1143. Longest Common Subsequence

https://leetcode.com/problems/longest-common-subsequence/
"""


class Solution:
    @staticmethod
    def longestCommonSubsequence(s1: str, s2: str) -> int:
        max_at = {}
        for c1 in s1:
            current_max = 0
            for i, c2 in enumerate(s2):
                potential_sum = current_max + 1
                current_max = max(current_max, max_at.get(i, 0))
                if c1 == c2:
                    max_at[i] = potential_sum
        return max(max_at.values(), default=0)


if __name__ == "__main__":
    inputs = (
        (("abcde", "ace"), 3),
        (("abc", "abc"), 3),
        (("abc", "def"), 0),
    )
    for input, expected in inputs:
        output = Solution.longestCommonSubsequence(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

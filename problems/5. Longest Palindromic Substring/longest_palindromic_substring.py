"""5. Longest Palindromic Substring.

Level: Medium

https://leetcode.com/problems/longest-palindromic-substring/
"""

# class Solution:
#     """This solution works, but much slower."""
#     @staticmethod
#     def longestPalindrome(s: str) -> str:
#         result = s[0]
#         for i, v in enumerate(s):
#             j = i + 1
#             while (j := s.find(v, j)) != -1:
#                 candidate = s[i : j + 1]
#                 if candidate == candidate[::-1]:
#                     result = result if len(result) >= len(candidate) else candidate
#                 j += 1

#         return result


class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:
        n = len(s)
        result = ""

        def expend(l: int, r: int) -> str:
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        for i in range(n):
            # first expand for odd len of s and second for even length
            result = max(expend(i, i), expend(i, i + 1), result, key=len)
        return result


if __name__ == "__main__":
    tests = (("babad", "aba"), ("cbbd", "bb"), ("a", "a"), ("ab", "b"), ("bb", "bb"))
    for input, expected in tests:
        output = Solution.longestPalindrome(input)
        assert output == expected, f"{input =}, {output =}, {expected =}"

    print("PASSED!!!")

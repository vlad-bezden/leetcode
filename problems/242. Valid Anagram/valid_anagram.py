"""242. Valid Anagram.

    Output
        isAnagram
        isAnagram took: 0.087963
        isAnagram took: 0.063295

        isAnagram_2
        isAnagram_2 took: 0.374750
        isAnagram_2 took: 0.347455

        isAnagram_3
        isAnagram_3 took: 0.326157
        isAnagram_3 took: 0.179309

        isAnagram_4
        isAnagram_4 took: 0.310831
        isAnagram_4 took: 0.168045

    Conclusion:
        Using sort is the fastest
"""
from timeit import timeit
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Sort both strings and compare them."""
        return sorted(s) == sorted(t)

    def isAnagram_2(self, s: str, t: str) -> bool:
        """Count chars using Counter."""
        return Counter(s) == Counter(t)

    def isAnagram_3(self, s: str, t: str) -> bool:
        """Count each char in the list for each char."""
        s_counter = [0] * 26
        t_counter = [0] * 26
        for i in range(len(s)):
            s_counter[ord(s[i]) - 97] += 1
            t_counter[ord(t[i]) - 97] += 1
        return s_counter == t_counter

    def isAnagram_4(self, s: str, t: str) -> bool:
        """Same as isAnagram_3 but using zip and chars instead of range."""
        s_counter = [0] * 26
        t_counter = [0] * 26
        for sc, tc in zip(s, t):
            s_counter[ord(sc) - 97] += 1
            t_counter[ord(tc) - 97] += 1
        return s_counter == t_counter


if __name__ == "__main__":
    inputs = [["anagram", "nagaram"], ["rat", "cat"]]
    expected = [True, False]

    solution = Solution()
    funcs = [
        solution.isAnagram,
        solution.isAnagram_2,
        solution.isAnagram_3,
        solution.isAnagram_4,
    ]

    for f in funcs:
        print(f"\n{f.__name__}")
        for input, expect in zip(inputs, expected):
            output = f(*input)
            assert output == expect, f"{expect=} {output=}"
            t = timeit(
                stmt=f"f('{input[0]}', '{input[1]}')",
                number=100_000,
                globals=globals(),
            )
            print(f"{f.__name__} took: {t:.6f}")

    print("\nPASSED!!!")

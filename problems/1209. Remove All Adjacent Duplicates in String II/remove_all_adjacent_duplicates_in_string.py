"""1209. Remove All Adjacent Duplicates in String II.

    Performance:
    Using string comparison (removeDuplicate):

    Output:
        Running: removeDuplicates
        removeDuplicates took: 0.099417
        removeDuplicates took: 0.398208
        removeDuplicates took: 0.826417
        removeDuplicates took: 0.037531
        removeDuplicates took: 0.151541
        removeDuplicates took: 0.136278

        Running: removeDuplicates_2
        removeDuplicates_2 took: 0.129090
        removeDuplicates_2 took: 0.518643
        removeDuplicates_2 took: 0.978547
        removeDuplicates_2 took: 0.034876
        removeDuplicates_2 took: 0.172249
        removeDuplicates_2 took: 0.178278

        Running: removeDuplicates_3
        removeDuplicates_3 took: 0.131957
        removeDuplicates_3 took: 0.413135
        removeDuplicates_3 took: 0.709120
        removeDuplicates_3 took: 0.114948
        removeDuplicates_3 took: 0.192088
        removeDuplicates_3 took: 0.277547
"""
from timeit import timeit


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """Creates new string of len 'k' and checks if substring is the same."""
        for i in range(len(s) - k, -1, -1):
            if s[i] * k == s[i : i + k]:
                s = s[:i] + s[i + k :]
        return s

    def removeDuplicates_2(self, s: str, k: int) -> str:
        """Using count function to check if all chars are the same."""
        for i in range(len(s) - k, -1, -1):
            if s[i : i + k].count(s[i]) == k:
                s = s[:i] + s[i + k :]
        return s

    def removeDuplicates_3(self, s: str, k: int) -> str:
        """Creates substrings that has to be replaced."""
        dist = set(s)
        to_remove = [c * k for c in dist]

        while True:
            start = s
            for c in to_remove:
                s = s.replace(c, "")
            # break while loop if there are no changes
            if s == start:
                return s


if __name__ == "__main__":
    solution = Solution()

    funcs = [
        solution.removeDuplicates,
        solution.removeDuplicates_2,
        solution.removeDuplicates_3,
    ]
    inputs = [
        ["abcd", 2],
        ["deeedbbcccbdaa", 3],
        ["pbbcggttciiippooaais", 2],
        ["aa", 3],
        ["aabb", 2],
        ["abcdd", 2],
    ]
    expected = ["abcd", "aa", "ps", "aa", "", "abc"]

    for f in funcs:
        print(f"\nRunning: {f.__name__}")
        for input, expect in zip(inputs, expected):
            output = f(*input)
            assert output == expect, f"{expect= }, {output= }"
            t = timeit(
                stmt=f"f('{input[0]}', {input[1]})",
                number=100_000,
                globals=globals(),
            )
            print(f"{f.__name__} took: {t:.6f}")

    print("\nPASSED!!!")

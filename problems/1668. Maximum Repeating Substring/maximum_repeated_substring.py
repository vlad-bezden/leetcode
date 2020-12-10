"""Maximum Repeated Substring.

    Using find is twice slower than you in:

    Output:
    
    Running maxRepeating
    maxRepeating took: 0.043529
    maxRepeating took: 0.032548
    maxRepeating took: 0.018079
    maxRepeating took: 0.132933

    Running maxRepeating_2
    maxRepeating_2 took: 0.085754
    maxRepeating_2 took: 0.067346
    maxRepeating_2 took: 0.030723
    maxRepeating_2 took: 0.204533

    PASSED!!!
"""

from timeit import timeit


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        counter = 1
        while word * counter in sequence:
            counter += 1
        return counter - 1

    def maxRepeating_2(self, sequence: str, word: str) -> int:
        counter = 1
        while sequence.find(word * counter) >= 0:
            counter += 1
        return counter - 1


if __name__ == "__main__":
    solution = Solution()

    inputs = [
        ("ababc", "ab"),
        ("ababc", "ba"),
        ("ababc", "ac"),
        (
            "aaabaaaabaaabaaaabaaaabaaaabaaaaba",
            "aaaba",
        ),
    ]
    expected = [2, 1, 0, 5]

    for f in [solution.maxRepeating, solution.maxRepeating_2]:
        print(f"\nRunning {f.__name__}")
        for input, expect in zip(inputs, expected):
            output = f(*input)
            assert output == expect, f"{input=}, {expect=}, {output=}"
            t = timeit(
                stmt=f"f('{input[0]}', '{input[1]}')", number=100_000, globals=globals()
            )
            print(f"{f.__name__} took: {t:.6f}")

    print("PASSED!!!")

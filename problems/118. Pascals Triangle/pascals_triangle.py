"""118. Pascal's Triangle

Performance Test:
generate_1 took: 0.3293
generate_2 took: 0.6331

Conclusion:
Using enumerator is twice faster than using range/indexing
"""

from timeit import timeit


class Solution:
    @staticmethod
    def generate_1(num_rows: int) -> list[list[int]]:
        """Using enumerator"""
        res = [[1]]

        for _ in range(1, num_rows):
            res.append([1] + [v + res[-1][i] for i, v in enumerate(res[-1][1:])] + [1])
        return res

    @staticmethod
    def generate_2(num_rows: int) -> list[list[int]]:
        """Using range/indexing"""
        res = [[1]]

        for row in range(1, num_rows):
            res.append([1] + [sum(res[-1][i : i + 2]) for i in range(0, row - 1)] + [1])
        return res


if __name__ == "__main__":
    inputs = ((5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]), (1, [[1]]))

    for input, expected in inputs:
        output = Solution.generate_1(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    s = Solution
    for f in [s.generate_1, s.generate_2]:
        t = timeit(stmt=f"f({20})", number=10_000, globals=globals())
        print(f"{f.__name__} took: {t:.4f}")

    print("PASSED!!!")

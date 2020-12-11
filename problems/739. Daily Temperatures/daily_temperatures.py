"""Daily Temperatures.

    Two solutions:
        1. Using stack DS
        2. Using dictionary/hash

    Outputs:
        dailyTemperatures    0.3449 sec
        dailyTemperatures_2  0.3190 sec
        dailyTemperatures_3  1.0231 sec
        dailyTemperatures    0.3515 sec
        dailyTemperatures_2  0.4171 sec
        dailyTemperatures_3  1.2873 sec
"""

from timeit import timeit


class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        """Using stack. The fastest solution."""
        results = [0] * len(temps)
        stack = []
        for i, t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                j = stack.pop()
                results[j] = i - j
            stack.append(i)
        return results

    def dailyTemperatures_2(self, temps: list[int]) -> list[int]:
        """Solution using stack. Iterating temperatures in reverse order."""
        n = len(temps)
        stack = []
        results = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and temps[stack[-1]] <= temps[i]:
                stack.pop()
            if stack:
                results[i] = stack[-1] - i
            stack.append(i)
        return results

    def dailyTemperatures_3(self, temps: list[int]) -> list[int]:
        t_indexes = {}
        n = len(temps)
        result = [0] * n
        for i in range(n - 1, -1, -1):
            t = temps[i]
            candidates = sorted(i_ for t_, i_ in t_indexes.items() if t_ > t)
            if candidates:
                result[i] = candidates[0] - i
            t_indexes[t] = i
        return result


if __name__ == "__main__":
    solution = Solution()

    inputs = [
        [73, 74, 75, 71, 69, 72, 76, 73],
        [89, 62, 70, 58, 47, 47, 46, 76, 100, 70],
    ]
    expected = [[1, 1, 4, 2, 1, 1, 0, 0], [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]]

    for input, expect in zip(inputs, expected):
        for f in [
            solution.dailyTemperatures,
            solution.dailyTemperatures_2,
            solution.dailyTemperatures_3,
        ]:
            output = f(input)
            assert output == expect, f"{input=}, {expect=}, {output=}"
            t = timeit(stmt=f"f({input})", number=100_000, globals=globals())
            print(f"{f.__name__:<20} {t:.4f} sec")

    print("\nPASSED!!!")

"""Range Addition

    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3814/
"""
from timeit import timeit
import numpy as np


class Solution:
    @staticmethod
    def getModifiedArray_numpy(length: int, updates: list[list[int]]) -> list[int]:
        arr = np.zeros(length, dtype=int)

        for start, end, increment in updates:
            arr[start : end + 1] += increment
        return arr.tolist()

    @staticmethod
    def getModifiedArray_naive(length: int, updates: list[list[int]]) -> list[int]:
        arr = [0] * length

        for start, end, increment in updates:
            for i in range(start, end + 1):
                arr[i] += increment
        return arr

    @staticmethod
    def getModifiedArray_fastest(length: int, updates: list[list[int]]) -> list[int]:
        """
        Update the start index, negative for index next to end index
        positive for start index, negative for index next to end index
        """
        arr = [0] * length
        for start, end, increment in updates:
            arr[start] += increment
            if end < length - 1:
                arr[end + 1] -= increment

        for i in range(1, length):
            arr[i] += arr[i - 1]

        return arr


if __name__ == "__main__":
    inputs = (
        ((5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]), [-2, 0, 3, 5, 3]),
        ((10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]]), [0, -4, 2, 2, 2, 4, 4, -4, -4, -4]),
    )
    for input, expected in inputs:
        for f in (
            Solution.getModifiedArray_numpy,
            Solution.getModifiedArray_naive,
            Solution.getModifiedArray_fastest,
        ):
            output = f(*input)
            assert output == expected, f"{input=}, {output=}, {expected=}"

            t = timeit(
                stmt=f"f({input[0]}, {input[1]})", number=1_000, globals=globals()
            )
            print(f"{f.__name__} took: {t:.4f}")

    print("PASSED!!!")

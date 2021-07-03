from bisect import insort_right
from operator import mul
from functools import reduce


def find_max_product(arr: list[int]) -> list[int]:
    sorted_list = []
    output = []
    for i, v in enumerate(arr):
        insort_right(sorted_list, v)
        output.append(-1 if i < 2 else reduce(mul, sorted_list[-3:]))
    return output


if __name__ == "__main__":
    inputs = [
        [[1, 2, 3, 4, 5], [-1, -1, 6, 24, 60]],
        [[2, 1, 2, 1, 2], [-1, -1, 4, 4, 8]],
        [[2, 4, 7, 1, 5, 3], [-1, -1, 56, 56, 140, 140]],
    ]

    for input, expected in inputs:
        result = find_max_product(input)
        assert result == expected, f"{input=}, {result=}, {expected=}"

    print("PASSED!!!")

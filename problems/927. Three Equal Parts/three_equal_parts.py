"""927. Three Equal Parts."""

from operator import indexOf


class Solution:
    @staticmethod
    def threeEqualParts(arr: list[int]) -> list[int]:
        no_ans = [-1, -1]
        numerator, denominator = divmod(sum(arr), 3)
        if not numerator and not denominator:
            # list of all 0's
            return [0, len(arr) - 1]
        if denominator:
            # it can't be split, number of 1's must be divisible by 3
            return no_ans
        # find trailing 0's
        zeros = indexOf(reversed(arr), 1)
        # find all 1's indexes
        ones_indexes = tuple(i for i, v in enumerate(arr) if v)
        # find start/end for each length of 1s
        p1s, p1e = ones_indexes[0], ones_indexes[numerator - 1]
        p2s, p2e = ones_indexes[numerator], ones_indexes[2 * numerator - 1]
        p3s, p3e = ones_indexes[2 * numerator], ones_indexes[-1]
        # get each part including leading 0's
        part1 = arr[p1s : p1e + 1 + zeros]
        part2 = arr[p2s : p2e + 1 + zeros]
        part3 = arr[p3s : p3e + 1 + zeros]
        # all parts has to be the same
        if part1 != part2 or part2 != part3:
            return no_ans
        return [p1e + zeros, p2e + zeros + 1]


if __name__ == "__main__":
    inputs = (
        ([1, 0, 1, 0, 1], [0, 3]),
        ([1, 1, 0, 1, 1], [-1, -1]),
        ([1, 1, 0, 0, 1], [0, 2]),
        ([1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1], [2, 8]),
        ([1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [3, 8]),
        ([1, 0, 1, 0, 0, 1, 0, 0], [-1, -1]),
        ([0, 0, 0, 0, 0], [0, 4]),
        ([0, 1, 0, 1, 1, 0, 1, 1, 0, 1], [3, 7]),
        ([1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [-1, -1]),
    )
    for input, expected in inputs:
        output = Solution.threeEqualParts(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

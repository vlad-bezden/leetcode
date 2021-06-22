from collections import Counter


class Solution:
    @staticmethod
    def canBeEqual(target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)


if __name__ == "__main__":
    inputs = [
        ([1, 2, 3, 4], [1, 4, 3, 2], True),
        ([1, 2, 3, 4], [1, 2, 3, 5], False),
        ([1, 1, 1, 2], [2, 2, 2, 1], False),
        ([7], [7], True),
        ([1, 1, 1, 1], [1, 1, 1, 1], True),
    ]

    for *input, expected in inputs:
        output = Solution.canBeEqual(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

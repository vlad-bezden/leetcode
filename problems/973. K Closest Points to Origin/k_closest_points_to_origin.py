from math import dist


class Solution:
    @staticmethod
    def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
        if k >= len(points):
            return points
        return sorted(points, key=lambda i: dist(i, [0, 0]))[:k]


if __name__ == "__main__":
    inputs = [
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
    ]

    for *input, expected in inputs:
        output = Solution.kClosest(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

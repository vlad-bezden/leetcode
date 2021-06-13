# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def get(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def dimensions(self) -> list[int]:
        return [len(self.matrix), len(self.matrix[0])]

    def __repr__(self):
        return str(self.matrix)


class Solution:
    @staticmethod
    def leftMostColumnWithOne(binaryMatrix: BinaryMatrix) -> int:
        rows, cols = binaryMatrix.dimensions()
        result = -1

        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1

        while current_row < rows and current_col > 0:
            if binaryMatrix.get(current_row, current_col):
                result = current_col
                left = 0
                # Use binary search to find leftmost 1 in current row
                while left < current_col:
                    mid = (left + current_col) // 2
                    if binaryMatrix.get(current_row, mid):
                        result = mid
                        current_col = mid
                    else:
                        left = mid + 1
            current_row += 1
        return result


if __name__ == "__main__":
    inputs = [
        [BinaryMatrix([[0, 0], [1, 1]]), 0],
        [BinaryMatrix([[0, 0], [0, 1]]), 1],
        [BinaryMatrix([[0, 0], [0, 0]]), -1],
        [BinaryMatrix([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]), 1],
        [
            BinaryMatrix(
                [
                    [1, 1, 1, 1, 1],
                    [0, 0, 0, 1, 1],
                    [0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                ]
            ),
            0,
        ],
        [
            BinaryMatrix(
                [
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                ]
            ),
            3,
        ],
    ]

    for input, expected in inputs:
        output = Solution.leftMostColumnWithOne(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

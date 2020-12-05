class Solution:
    SPAN = 3

    def candyCrush(self, board: list[list[int]]) -> list[list[int]]:
        while True:
            # holds items to be crushed
            flaged = self.crush(board)
            # validate items horizontally
            board_t = [[*x] for x in zip(*board)]
            # validate items vertically
            flaged |= self.crush(board_t, True)
            if flaged:
                board = self.gravity(board, flaged)
            else:
                return board

    @staticmethod
    def gravity(
        board: list[list[int]], flaged: set[tuple[int, int]]
    ) -> list[list[int]]:
        """If there are empty spaces, drop candies on the top.

        After crushing all candies simultaneously,
        if an empty space on the board has candies on top of itself,
        then these candies will drop until they hit a candy or bottom
        at the same time. (No new candies will drop outside the top boundary.)
        """

        # transpose matrix 90 degrees
        board_t = [[*x] for x in zip(*board)]
        row_len = len(board_t[0])
        for ix, iy in sorted(flaged, reverse=True):
            del board_t[iy][ix]
        for idx, row in enumerate(board_t):
            row_diff = row_len - len(row)
            if row_diff:
                board_t[idx] = [0] * row_diff + row
        # transpose matrix back to original
        return [[*x] for x in zip(*board_t)]

    @staticmethod
    def crush(board: list[list[int]], transposed: bool = False):
        """Finds 3 or more horizontal values and adds them to flaged."""
        flaged = set()
        row_len = len(board[0])
        for ix, row in enumerate(board):
            for iy, col in enumerate(row[: row_len - Solution.SPAN + 1]):
                if col != 0 and len(set(row[iy : iy + Solution.SPAN])) == 1:
                    while iy < row_len and col == row[iy]:
                        flaged.add((iy, ix) if transposed else (ix, iy))
                        iy += 1
                    if iy == row_len:
                        break
        return flaged


s = Solution()
board = [
    [110, 5, 112, 113, 114],
    [210, 211, 5, 213, 214],
    [310, 311, 3, 313, 314],
    [410, 411, 412, 5, 414],
    [5, 1, 512, 3, 3],
    [610, 4, 1, 613, 614],
    [710, 1, 2, 713, 714],
    [810, 1, 2, 1, 1],
    [1, 1, 2, 2, 2],
    [4, 1, 4, 4, 1014],
]
result = s.candyCrush(board)
expected = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [110, 0, 0, 0, 114],
    [210, 0, 0, 0, 214],
    [310, 0, 0, 113, 314],
    [410, 0, 0, 213, 414],
    [610, 211, 112, 313, 614],
    [710, 311, 412, 613, 714],
    [810, 411, 512, 713, 1014],
]

assert result == expected
rows, cols = 5, 10
board = [[y + 1 + x * cols for y in range(cols)] for x in range(rows)]
result = s.candyCrush(board)
assert result == board
rows, cols = 3, 3
board = [[y + 1 + x * cols for y in range(cols)] for x in range(rows)]
result = s.candyCrush(board)
assert result == board

print("PASSED!!!")

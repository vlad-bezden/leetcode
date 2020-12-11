"""Number of Islands.

    Outputs:
        numIslands_2    0.0218 sec
        numIslands      0.0030 sec
        numIslands_2    0.0196 sec
        numIslands      0.0028 sec
        numIslands_2    0.0038 sec
        numIslands      0.0011 sec
        numIslands_2    0.0013 sec
        numIslands      0.0011 sec
        numIslands_2    0.0012 sec
        numIslands      0.0009 sec
"""
from timeit import timeit


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """Using DFS and changing visited cells to 0."""
        self.grid, self.rows, self.cols = grid, len(grid), len(grid[0])
        islands = 0
        for cell in (
            (x, y) for x, row in enumerate(grid) for y, v in enumerate(row) if v == "1"
        ):
            islands += 1
            self._conquer_island(*cell)
        return islands

    def _conquer_island(self, x, y):
        """Check if cell is island (1) and if it's mark it as water (0)."""
        if x < 0 or y < 0 or self.rows <= x or self.cols <= y or self.grid[x][y] == "0":
            return
        self.grid[x][y] = "0"
        self._conquer_island(x - 1, y)
        self._conquer_island(x + 1, y)
        self._conquer_island(x, y - 1)
        self._conquer_island(x, y + 1)

    def numIslands_2(self, grid: list[list[str]]) -> int:
        """Without modifying original grid.

        Keeps track of visited and that needs to be visited cells
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        islands = 0

        for cell in (
            (x, y)
            for x, row in enumerate(grid)
            for y, v in enumerate(row)
            if v == "1" and (x, y) not in self.visited
        ):
            # this is a new island
            islands += 1
            self._conquer_island_2(*cell)
        return islands

    def _conquer_island_2(self, x, y) -> None:
        """Finds neighbors to be visited."""
        xy = (x, y)
        if (
            x < 0
            or y < 0
            or self.rows <= x
            or self.cols <= y
            or xy in self.visited
            or self.grid[x][y] == "0"
        ):
            return
        self.visited.add(xy)
        self._conquer_island_2(x - 1, y)
        self._conquer_island_2(x + 1, y)
        self._conquer_island_2(x, y - 1)
        self._conquer_island_2(x, y + 1)


if __name__ == "__main__":
    s = Solution()
    inputs = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        [["1"]],
        [["0", "0"]],
        [[]],
    ]
    expected = [1, 3, 1, 0, 0]
    funcs = [s.numIslands_2, s.numIslands]

    for f, input, expect in (
        (f, i, r) for i, r in zip(inputs, expected) for f in funcs
    ):
        output = f(input)
        assert output == expect, f"{input=}, {expect=}, {output=}"

        # performance test
        t = timeit(stmt=f"f({input})", number=1_000, globals=globals())
        print(f"{f.__name__:<15} {t:.4f} sec")

    print("\nPASSED!!!")

"""827. Making A Large Island.

https://leetcode.com/problems/making-a-large-island/
"""


class Solution:
    @staticmethod
    def largestIsland(grid: list[list[int]]) -> int:
        size = len(grid)
        # neighbors coordinates
        near = lambda r, c: ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))

        def neighbors(row: int, col: int):
            for n_row, n_col in near(row, col):
                if 0 <= n_row < size and 0 <= n_col < size:
                    yield n_row, n_col

        def dfs(row: int, col: int, index: int) -> int:
            ans = 1
            grid[row][col] = index
            for n_row, n_col in neighbors(row, col):
                if grid[n_row][n_col] == 1:
                    ans += dfs(n_row, n_col, index)
            return ans

        area = {}
        index = 2
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 1:
                    area[index] = dfs(i, j, index)
                    index += 1

        ans = max(area.values() or [0])
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 0:
                    seen = {
                        grid[n_row][n_col]
                        for n_row, n_col in neighbors(i, j)
                        if grid[n_row][n_col] > 1
                    }
                    ans = max(ans, 1 + sum(area[i] for i in seen))

        return ans


if __name__ == "__main__":
    inputs = (
        ([[1, 0], [0, 1]], 3),
        ([[1, 1], [1, 0]], 4),
        ([[1, 1], [1, 1]], 4),
        (
            [
                [1, 1, 0, 1, 1],
                [1, 1, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1],
            ],
            9,
        ),
    )

    for input, expected in inputs:
        output = Solution.largestIsland(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

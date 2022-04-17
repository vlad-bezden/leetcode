"""1275. Find Winner on a Tic Tac Toe Game.

Level: Easy


https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
"""

SIZE = 3
WIN_VALUES = [
    7,
    56,
    73,
    84,
    146,
    273,
    292,
    448,
]
# cell values 1, 2, 4, 8, 16, 32, 64, etc
MOVES_VALUES = {(r, c): 2 ** (r * SIZE + c) for c in range(SIZE) for r in range(SIZE)}


class Solution:
    @staticmethod
    def tictactoe(moves: list[list[int]]) -> str:
        for i, player in enumerate("AB"):
            score = sum(MOVES_VALUES[tuple(m)] for m in moves[i::2])
            if any(score & w == w for w in WIN_VALUES):
                return player
        if len(moves) < SIZE ** 2:
            return "Pending"
        return "Draw"


if __name__ == "__main__":
    solution = Solution()
    tests = (
        ([[1, 2], [2, 1], [1, 0], [0, 0], [0, 1], [2, 0], [1, 1]], "A"),
        ([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], "A"),
        (
            [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]],
            "Draw",
        ),
        ([[0, 0], [1, 1]], "Pending"),
    )
    for test in tests:
        input, expected = test
        result = solution.tictactoe(input)
        assert result == expected

    print("PASSED!!!")

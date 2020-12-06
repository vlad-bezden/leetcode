class Solution:
    def transpose(self, A: list[list[int]]) -> list[list[int]]:
        # using list comprehension
        return [[row[c] for row in A] for c in range(len(A[0]))]

    def transpose_2(self, A: list[list[int]]) -> list[list[int]]:
        # using zip
        return [list(x) for x in zip(*A)]

    def transpose_3(self, A: list[list[int]]) -> list[list[int]]:
        # pure manual implementation
        rows = len(A)
        cols = len(A[0])
        T = [[0] * rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                T[c][r] = A[r][c]
        return T


if __name__ == "__main__":
    s = Solution()

    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    output = s.transpose(input)
    assert output == expected

    input = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    output = s.transpose(input)
    assert output == expected

    print("PASSED!!!")

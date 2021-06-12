class Solution:
    @staticmethod
    def isAlienSorted(words: list[str], order: str) -> bool:
        mapper = {c: i for i, c in enumerate(order)}
        indexes = [[mapper[c] for c in word] for word in words]
        return indexes == sorted(indexes)


if __name__ == "__main__":
    inputs = [
        [["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True],
        [["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False],
        [["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False],
        [["alien", "alien"], "abcdefghijklmnopqrstuvwxyz", True],
        [["hello"], "abcdefghijklmnopqrstuvwxyz", True],
    ]

    solution = Solution()
    for words, order, expected in inputs:
        output = solution.isAlienSorted(words, order)
        assert output == expected, f"{expected=}, {output=}"

    print("PASSED!!!")

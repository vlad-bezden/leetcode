"""937. Reorder Data in Log Files"""


class Solution:
    @staticmethod
    def reorderLogFiles(logs: list[str]) -> list[str]:
        def compare(log: str):
            identifier, tail = log.split(" ", maxsplit=1)
            return (0, tail, identifier) if tail[0].isalpha() else (1,)

        return sorted(logs, key=compare)


if __name__ == "__main__":
    inputs = [
        [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ],
        ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],
    ]
    expected = [
        [
            "let1 art can",
            "let3 art zero",
            "let2 own kit dig",
            "dig1 8 1 5 1",
            "dig2 3 6",
        ],
        ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"],
    ]

    for input, expect in zip(inputs, expected):
        output = Solution.reorderLogFiles(input)
        assert output == expect, f"{input=}, {expect=}, {output=}"

    print("\nPASSED!!!")

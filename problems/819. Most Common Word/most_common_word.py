"""819. Most Common Word."""
from string import punctuation
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.translate(str.maketrans(dict.fromkeys(punctuation, " ")))
        counter = Counter(w for w in paragraph.lower().split() if w not in banned)
        return counter.most_common(1)[0][0]


if __name__ == "__main__":
    s = Solution()

    inputs = [
        ["Bob hit a ball, the hit BALL flew far after it was hit.", "hit"],
        ["a, a, a, a, b,b,b,c, c", "a"],
    ]
    expected = ["ball", "b"]

    for input, expect in zip(inputs, expected):
        output = s.mostCommonWord(*input)
        assert output == expect, f"{input=}, {expect=}, {output=}"

    print("\nPASSED!!!")

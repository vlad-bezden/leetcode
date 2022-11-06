"""472. Concatenated Words.

Level: Hard

https://leetcode.com/problems/concatenated-words/
"""


from functools import cache


class Solution:
    @staticmethod
    def findAllConcatenatedWordsInADict(words: list[str]) -> list[str]:
        words_set = set(words)

        @cache
        def is_concat(word):
            for i in range(1, len(word)):
                head, tail = word[:i], word[i:]
                if head in words_set and (tail in words_set or is_concat(tail)):
                    return True
            return False

        return [word for word in words if is_concat(word)]


if __name__ == "__main__":
    tests = (
        (
            [
                "cat",
                "cats",
                "catsdogcats",
                "dog",
                "dogcatsdog",
                "hippopotamuses",
                "rat",
                "ratcatdogcat",
            ],
            ["catsdogcats", "dogcatsdog", "ratcatdogcat"],
        ),
        (["cat", "dog", "catdog"], ["catdog"]),
        (["a", "b", "ab", "abc"], ["ab"]),
    )
    for test in tests:
        input, expected = test
        output = Solution.findAllConcatenatedWordsInADict(input)
        assert set(output) == set(expected), f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

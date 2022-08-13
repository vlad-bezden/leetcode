"""1816. Truncate Sentence.

Level: Easy

https://leetcode.com/problems/truncate-sentence/
"""


class Solution:
    @staticmethod
    def truncateSentence(s: str, k: int) -> str:
        if not s:
            return s
        return " ".join(s.split()[:k])


if __name__ == "__main__":
    tests = (
        (("Hello how are you Contestant", 4), "Hello how are you"),
        (("What is the solution to this problem", 4), "What is the solution"),
        (("chopper is not a tanuki", 5), "chopper is not a tanuki"),
        (("", 2), ""),
        ((None, 2), None),
    )

    for test in tests:
        input, expected = test
        result = Solution.truncateSentence(*input)
        assert result == expected, f"{input = }, {result =}, {expected =}"

    print("PASSED!!!")

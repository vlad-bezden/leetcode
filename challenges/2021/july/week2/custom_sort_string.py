"""Custom Sort String

    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3813/
"""


class Solution:
    @staticmethod
    def customSortString(order: str, str: str) -> str:
        letters_mapper = {c: i for i, c in enumerate(order)}
        # 26 chars + 1 for storing all chars that are not in the order
        buckets = [[] for _ in range(26 + 1)]

        for c in str:
            # all chars that map to mapper goes to their buckets
            # the chars that are not in the mapper goes to the last bucket
            buckets[letters_mapper.get(c, 26)].append(c)
        return "".join("".join(c) for c in buckets if c)


if __name__ == "__main__":
    inputs = ((("cba", "abcd"), "cbad"),)
    for input, expected in inputs:
        output = Solution.customSortString(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

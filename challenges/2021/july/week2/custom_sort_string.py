"""Custom Sort String

    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3813/

    "Your runtime beats 100% of python3 submissions"
"""


class Solution:
    @staticmethod
    def customSortString(order: str, str: str) -> str:
        """Sort string in custom order based on 'order' spec

        All letters that are in order will be sorted based on letters_mapper
        and any letter that is not in the mapper will be assigned value beyond
        number of characters in English alphabet
        """
        letters_mapper = {c: i for i, c in enumerate(order)}
        return "".join(sorted(str, key=lambda c: letters_mapper.get(c, 27)))


if __name__ == "__main__":
    inputs = ((("cba", "abcd"), "cbad"),)
    for input, expected in inputs:
        output = Solution.customSortString(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

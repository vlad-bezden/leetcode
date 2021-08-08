"""14. Longest Common Prefix.

https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    @staticmethod
    def longestCommonPrefix(strings: list[str]) -> str:
        if len(strings) == 1:
            return strings[0]
        answer = ""
        for chars in zip(*strings):
            if len(set(chars)) == 1:
                answer += chars[0]
            else:
                break
        return answer


if __name__ == "__main__":
    inputs = (
        (["", ""], ""),
        (["flower", ""], ""),
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["dog", "dogma", "dogtrine"], "dog"),
        (["dog", "doom", "drum"], "d"),
    )

    for input, expected in inputs:
        output = Solution.longestCommonPrefix(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

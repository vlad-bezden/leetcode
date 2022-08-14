"""49. Group Anagrams.

Level: Medium

https://leetcode.com/problems/group-anagrams/
"""


class Solution:
    @staticmethod
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        map_: dict[str, list[str]] = {}
        for s in strs:
            map_.setdefault("".join(sorted(s)), []).append(s)
        return [*map_.values()]


if __name__ == "__main__":
    tests = (
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
    )
    for test in tests:
        input, expected = test
        output = Solution.groupAnagrams(input)
        assert output == expected, f"{input =}, {output =}, {expected =}"

    print("PASSED!!!")

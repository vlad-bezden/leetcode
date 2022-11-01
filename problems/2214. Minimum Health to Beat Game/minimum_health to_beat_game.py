"""2214. Minimum Health to Beat Game.

Level: Medium

Explanation: https://leetcode.com/problems/minimum-health-to-beat-game/discuss/1914467/Python-4-liner-simple-solution-O(n)-O(1)

https://leetcode.com/problems/minimum-health-to-beat-game/
"""


class Solution:
    @staticmethod
    def minimumHealth(damage: list[int], armor: int) -> int:
        return sum(damage) - min(max(damage), armor) + 1


if __name__ == "__main__":
    tests = (
        (([2, 7, 4, 3], 4), 13),
        (([2, 7, 5, 3], 4), 15),
        (([2, 5, 3, 4], 7), 10),
        (([3, 3, 3], 0), 10),
    )
    for test in tests:
        input, expected = test
        output = Solution.minimumHealth(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

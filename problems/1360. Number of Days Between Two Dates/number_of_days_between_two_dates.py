"""1360. Number of Days Between Two Dates.

Level: Easy

https://leetcode.com/problems/number-of-days-between-two-dates/
"""

from datetime import datetime


class Solution:
    @staticmethod
    def daysBetweenDates(date1: str, date2: str) -> int:
        return abs(
            datetime.fromisoformat(date2)
            - datetime.fromisoformat(date1)
        ).days


if __name__ == "__main__":
    tests = ((("2019-06-29", "2019-06-30"), 1), (("2020-01-15", "2019-12-31"), 15))
    for test in tests:
        input, expected = test
        result = Solution.daysBetweenDates(*input)
        assert result == expected

    print("PASSED!!!")

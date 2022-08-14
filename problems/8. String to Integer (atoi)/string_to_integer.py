"""8. String to Integer (atoi).

Level: Medium

https://leetcode.com/problems/string-to-integer-atoi/
"""

from curses.ascii import isdigit

MIN_VAL = -(2**31)
MAX_VAL = 2**31 - 1


class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        sign = 1
        ls = [*s.strip()]
        if not ls:
            return 0
        if (s := ls[0]) in "+-":
            if s == "-":
                sign = -1
            ls = ls[1:]
        i = res = 0
        n = len(ls)
        ord_0 = ord("0")
        while i < n and isdigit(ls[i]):
            res = res * 10 + ord(ls[i]) - ord_0
            i += 1
        return max(MIN_VAL, min(res * sign, MAX_VAL))


if __name__ == "__main__":
    tests = (
        ("42", 42),
        ("  -42", -42),
        ("  +42", 42),
        ("  ++42", 0),
        ("4193 with words", 4193),
        ("123.87", 123),
        ("4000000000", 2147483647),
        ("", 0),
        ("-23a45 567 v", -23),
        ("123 45 567 v", 123),
    )
    for test in tests:
        input, expected = test
        output = Solution.myAtoi(input)
        assert output == expected, f"{input =}, {output =}, {expected =}"

    print("PASSED!!!")

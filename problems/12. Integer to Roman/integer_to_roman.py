"""12. Integer to Roman.

Level: Medium

https://leetcode.com/problems/integer-to-roman/
"""


class Solution:
    INT_TO_ROMAN = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (3, "III"),
        (2, "II"),
        (1, "I"),
    ]

    @staticmethod
    def intToRoman(num: int) -> str:
        result = []
        for k, v in Solution.INT_TO_ROMAN:
            # exit if there is no more conversion left
            if num == 0:
                break
            q, num = divmod(num, k)
            if q:
                result.append(q * v)
        return "".join(result)


if __name__ == "__main__":
    tests = (
        (7, "VII"),
        (3, "III"),
        (58, "LVIII"),
        (78, "LXXVIII"),
        (1994, "MCMXCIV"),
        (1973, "MCMLXXIII"),
    )
    for test in tests:
        input, expected = test
        output = Solution.intToRoman(input)
        assert output == expected, f"{input =}, {output =}, {expected =}"

    print("PASSED!!!")

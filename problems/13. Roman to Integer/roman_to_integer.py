"""13. Roman to Integer.

https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    ROMAN_TO_INT = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    @staticmethod
    def romanToInt(roman: str) -> int:
        arabic = 0
        temp = ""
        for char in roman:
            if temp + char not in Solution.ROMAN_TO_INT:
                arabic += Solution.ROMAN_TO_INT[temp]
                temp = ""
            temp += char
        arabic += Solution.ROMAN_TO_INT[temp]
        return arabic


if __name__ == "__main__":
    inputs = (
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    )

    for input, expected in inputs:
        output = Solution.romanToInt(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

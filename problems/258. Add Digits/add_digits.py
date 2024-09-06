"""258. Add Digits"""


class Solution:
    @staticmethod
    def addDigits(num: int) -> int:
        while num > 9:
            num = sum(divmod(num, 10))
        return num


if __name__ == "__main__":
    tests = ((38, 2), (0, 0), (246, 3), (478, 1))

    for input, expected in tests:
        output = Solution.addDigits(input)
        assert output == expected, f"{input = }, {output = }, {expected = }"

    print("PASSED!!!")

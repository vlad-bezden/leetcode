class Solution:
    ORD_0 = 48

    @staticmethod
    def addStrings(num1: str, num2: str) -> str:
        def to_num(num: str) -> int:
            l = len(num)
            return sum(
                10 ** (l - i - 1) * (ord(num[i]) - Solution.ORD_0) for i in range(l)
            )

        return str(to_num(num1) + to_num(num2))


if __name__ == "__main__":
    inputs = [(("11", "123"), "134"), (("456", "77"), "533"), (("0", "0"), "0")]

    for input, expected in inputs:
        output = Solution.addStrings(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

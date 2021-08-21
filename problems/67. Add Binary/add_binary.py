"""67. Add Binary.

https://leetcode.com/problems/add-binary/
"""


class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        answer = []
        carry = 0

        for i in reversed(range(max_len)):
            r = carry
            r += 1 if a[i] == "1" else 0
            r += 1 if b[i] == "1" else 0

            answer.append("0" if r == 0 or r == 2 else "1")
            carry = 0 if r < 2 else 1

        if carry:
            answer.append("1")
        answer.reverse()

        return "".join(answer)


if __name__ == "__main__":
    inputs = (({"a": "11", "b": "1"}, "100"), ({"a": "1010", "b": "1011"}, "10101"))
    for input, expected in inputs:
        output = Solution.addBinary(**input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

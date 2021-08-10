"""1047. Remove All Adjacent Duplicates In String.

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""


class Solution:
    @staticmethod
    def removeDuplicates(s: str) -> str:
        output = []
        for char in s:
            if output and char == output[-1]:
                output.pop()
            else:
                output.append(char)
        return "".join(output)


if __name__ == "__main__":
    inputs = (
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
        ("xx", ""),
        ("xxx", "x"),
        ("xxxx", ""),
        ("abcdefgh", "abcdefgh"),
        ("x", "x"),
    )

    for input, expected in inputs:
        output = Solution.removeDuplicates(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

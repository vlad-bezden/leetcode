"""20. Valid Parentheses."""


class Solution:
    BRACKETS = "{}()[]"

    def isValid(self, s: str) -> bool:
        it = iter(self.BRACKETS)
        pairs = dict(zip(it, it))
        stack = []
        for b in s:
            if b in pairs:
                stack.append(b)
            elif not stack or b != pairs[stack.pop()]:
                return False
        return not stack


if __name__ == "__main__":
    inputs = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    expected = [True, True, False, False, True]

    solution = Solution()

    for input, expect in zip(inputs, expected):
        output = solution.isValid(input)
        assert output is expect, f"{input=}, {output=}, {expect=}"

    print("\nPASSED!!!")

class Solution:
    @staticmethod
    def minRemoveToMakeValid(s: str) -> str:
        word = list(s)
        stack = []
        for i, c in enumerate(word):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    word[i] = ""

        while stack:
            word[stack.pop()] = ""

        return "".join(word)


if __name__ == "__main__":
    inputs = [
        ["lee(t(c)o)de)", "lee(t(c)o)de"],
        ["a)b(c)d", "ab(c)d"],
        ["))((", ""],
        ["(a(b(c)d)", "a(b(c)d)"],
    ]

    for input, expected in inputs:
        output = Solution.minRemoveToMakeValid(input)
        assert output == expected, f"{output=}, {expected=}"

    print("PASSED!!!")

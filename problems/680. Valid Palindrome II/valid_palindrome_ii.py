class Solution:
    @staticmethod
    def validPalindrome(text: str) -> bool:
        del_char = lambda i: text[:i] + text[i + 1:]
        is_palindrome = lambda s: s == s[::-1]
        if is_palindrome(text):
            return True
        l = len(text)
        mid = l // 2
        for i, j in zip(range(mid), range(l - 1, mid, -1)):
            # first char that is not the same on both sides
            if text[i] != text[j]:
                return is_palindrome(del_char(i)) or is_palindrome(del_char(j))
        return True


if __name__ == "__main__":
    inputs = (
        ("aba", True),
        ("abca", True),
        ("abc", False),
        ("axbcdcba", True),
        ("abcxcba", True),
        ("abcxcab", False),
        ("abcxcbea", True)
    )

    for input, expected in inputs:
        output = Solution.validPalindrome(input)
        assert output == expected, f"{input=}, {expected=}, {output=}"

    print("PASSED!!!")

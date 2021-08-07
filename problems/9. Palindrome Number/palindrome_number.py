"""9. Palindrome Number

https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed = 0
        tmp = x
        while tmp:
            tmp, reminder = divmod(tmp, 10)
            reversed = reversed * 10 + reminder
        return reversed == x


if __name__ == "__main__":
    inputs = (
        (121, True),
        (-121, False),
        (10, False),
        (5, True),
        (0, True),
    )

    for input, expected in inputs:
        output = Solution.isPalindrome(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

"""696. Count Binary Substrings.

Level: Easy

https://leetcode.com/problems/count-binary-substrings/
"""


class Solution:
    @staticmethod
    def countBinarySubstrings(s: str) -> int:
        current = 1
        prev = 0
        result = 0

        for p, c in zip(s, s[1:]):
            if p != c:
                result += min(current, prev)
                prev, current = current, 1
            else:
                current += 1
        return min(current, prev) + result


if __name__ == "__main__":
    assert 6 == Solution.countBinarySubstrings("00110011")
    assert 4 == Solution.countBinarySubstrings("10101")
    assert 1 == Solution.countBinarySubstrings("01")
    assert 0 == Solution.countBinarySubstrings("")

    print("PASSED!!!")

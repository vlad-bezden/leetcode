"""696. Count Binary Substrings.

https://leetcode.com/problems/count-binary-substrings/
"""


class Solution:
    @staticmethod
    def countBinarySubstrings(string: str) -> int:
        result = 0
        prev = 0
        current = 1
        for i, c in enumerate(string[1:]):
            if string[i] != c:
                result += min(prev, current)
                prev = current
                current = 1
            else:
                current += 1
        return result + min(prev, current)


if __name__ == "__main__":
    assert 6 == Solution.countBinarySubstrings("00110011")
    assert 4 == Solution.countBinarySubstrings("10101")
    assert 1 == Solution.countBinarySubstrings("01")
    assert 0 == Solution.countBinarySubstrings("")

    print("PASSED!!!")

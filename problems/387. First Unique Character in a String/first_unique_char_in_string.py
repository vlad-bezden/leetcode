from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, j in Counter(s).items():
            if j == 1:
                return s.index(i)
        return -1


if __name__ == "__main__":
    s = Solution()

    result = s.firstUniqChar("leetcode")
    assert 0 == result

    result = s.firstUniqChar("loveleetcode")
    assert 2 == result

    result = s.firstUniqChar("aabbccddeeffgg")
    assert -1 == result

    result = s.firstUniqChar("dddccdbba")
    assert 8 == result, f"Expected: 8, actual {result}"

    print("PASSED!!!")

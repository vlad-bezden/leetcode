"""Isomorphic Strings
    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3811/
"""


class Solution:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        if not s or not t and len(s) != len(t):
            return False

        hash = {}
        visited = set()

        for a, b in zip(s, t):
            # check if `a` already mapped to `b`
            if c := hash.get(a):
                # check if `a` maps to the same char as before
                if c != b:
                    return False
            elif b in visited:
                # new chars, check if `b` already mapped to different char in `s`
                return False
            # new char `a`, map it to `b`
            else:
                hash[a] = b
                visited.add(b)

        return True


if __name__ == "__main__":
    inputs = (
        (("egg", "add"), True),
        (("foo", "bar"), False),
        (("paper", "title"), True),
    )
    for input, expected in inputs:
        output = Solution.isIsomorphic(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

"""Push Dominoes.

    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3821/
"""


class Solution:
    @staticmethod
    def pushDominoes(dominoes: str) -> str:
        force = length = len(dominoes)
        tmp = 0
        # initially there are no forces 0 == .
        forces = [0] * length
        # calculate dominoes falling/force to the right
        # force to the right is decreasing by 1 for each domino
        for i, v in enumerate(dominoes):
            if v == "R":
                tmp = force
            elif v == "L":
                tmp = 0
            forces[i] = max(tmp, 0)
            tmp -= 1
        tmp = 0
        # calculate dominoes falling/forcing to the left
        # force to the left is opposite than right and it is negative force
        for i, v in reversed(list(enumerate(dominoes))):
            if v == "L":
                tmp = -force
            elif v == "R":
                tmp = 0
            forces[i] += min(tmp, 0)
            tmp += 1
        # here we have all dominoes forces for positive it's R for negative it's L
        # and if force is 0 then it's .
        return "".join(["R" if n > 0 else "L" if n < 0 else "." for n in forces])


if __name__ == "__main__":

    inputs = (
        ("RR.L", "RR.L"),
        (".L.R...LR..L..", "LL.RR.LLRRLL.."),
        ("R..L", "RRLL"),
        ("R...L", "RR.LL"),
        ("R..R..", "RRRRRR"),
        ("....", "...."),
        ("L..", "L.."),
        ("R..", "RRR"),
        ("..L", "LLL"),
        ("..L..", "LLL.."),
        (".R.L.", ".R.L."),
        (".L.R.", "LL.RR"),
    )
    for input, expected in inputs:
        output = Solution.pushDominoes(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

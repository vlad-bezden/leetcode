from collections import Counter
from math import inf


def min_length_substrings(s: str, t: str) -> int:
    output = inf
    l_pointer = 0
    lookup = Counter(t)
    d_len = len(t)
    for i, c in enumerate(s):
        if c in lookup:
            lookup[c] -= 1
            if lookup[c] >= 0:
                d_len -= 1
        while d_len == 0:
            output = min(output, i - l_pointer + 1)
            nc = s[l_pointer]
            l_pointer += 1
            if nc in lookup:
                lookup[nc] += 1
                if lookup[nc] > 0:
                    d_len += 1
    return output if output != inf else -1


if __name__ == "__main__":
    inputs = [
        # {"d": [0], "f": [4]}
        (["dcbefebce", "fd"], 5),
        (["dddcbefedce", "fd"], 3),
        # {"d":[0, 1, 4, 8], "f": [6]}
        (["ddcbdefedce", "fdd"], 5),
        # {"d": [0, 1, 2, 7], "f": [6]}
        (["dddcbefdece", "fdd"], 6),
        # {"d": [0, 2, 3, 8], "f": [1, 7]}
        (["dfddcbefdece", "ffd"], 7),
        # {"d": [0, 2, 7, 10], "f": [5, 9]}
        (["dcdeefedcfd", "fd"], 2),
        (["bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf", "cbccfafebccdccebdd"], -1),
    ]

    for input, expected in inputs:
        result = min_length_substrings(*input)
        assert result == expected, f"{input=}, {result=}, {expected=}"

    print("PASSED!!!")

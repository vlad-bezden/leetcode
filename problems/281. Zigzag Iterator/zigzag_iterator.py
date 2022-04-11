"""281. Zigzag Iterator.

Lever: Medium

https://leetcode.com/problems/zigzag-iterator/
"""

from itertools import chain, zip_longest


class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]) -> None:
        self.n = len(v1) + len(v2)
        self.data = filter(
            lambda i: i is not None, chain.from_iterable(zip_longest(v1, v2))
        )

    def next(self) -> int:
        self.n -= 1
        return next(self.data)

    def hasNext(self) -> bool:
        return self.n > 0


if __name__ == "__main__":
    tests = (
        (([1, 2], [3, 4, 5, 6]), [1, 3, 2, 4, 5, 6]),
        (([1], []), [1]),
        (([], [1]), [1]),
    )
    for test in tests:
        input, expected = test
        zigzag = ZigzagIterator(*input)
        result = []
        while zigzag.hasNext():
            result.append(zigzag.next())
        assert result == expected

    print("PASSED!!!")

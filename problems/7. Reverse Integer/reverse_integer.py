"""7. Reverse Integer."""

from timeit import timeit


class Solution:
    def reverse(self, x: int) -> int:
        x = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return 0 if x >= 2 ** 31 - 1 or x <= -(2 ** 31) else x

    def reverse_2(self, x: int) -> int:
        """Using string to reverse digits."""
        sign = -1 if x < 0 else 1
        x *= sign
        # remove trailing 0s
        while x and x % 10 == 0:
            x //= 10
        x = int(str(x)[::-1]) * sign
        return 0 if x >= 2 ** 31 - 1 or x <= -(2 ** 31) else x

    def reverse_3(self, x: int) -> int:
        """Using integer to divide number by 10."""
        answer = 0
        sign = -1 if x < 0 else 1
        x *= sign
        while x:
            x, r = divmod(x, 10)
            answer = answer * 10 + r
        answer *= sign
        return 0 if answer >= 2 ** 31 - 1 or answer <= -(2 ** 31) else answer


if __name__ == "__main__":
    solution = Solution()
    inputs = [123, -123, 120, 0, 1534236469]
    expected = [321, -321, 21, 0, 0]

    funcs = [
        solution.reverse,
        solution.reverse_2,
        solution.reverse_3,
    ]
    for f, input, expect in (
        (f, i, e) for i, e in zip(inputs, expected) for f in funcs
    ):
        print(f"\nRunning {f.__name__}, {input=}")
        output = f(input)
        assert output == expect, f"{input=}, {expect=}, {output=}"
        t = timeit(
            stmt=f"f({input})",
            number=10_000,
            globals=globals(),
        )
        print(f"{f.__name__} took: {t:.6f}")

    print("PASSED!!!")

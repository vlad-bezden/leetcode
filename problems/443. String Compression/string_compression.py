"""443. String Compression."""
from timeit import timeit


class Solution:
    def compress(self, chars: list[str]) -> int:
        """Using 'chars' as an immutable storage.

        Time complexity O(N)
        Space complexity O(1)
        """
        counter = 1
        for i in range(len(chars) - 1, -1, -1):
            if i and chars[i] == chars[i - 1]:
                chars.pop(i)
                counter += 1
            else:
                if counter > 1:
                    for j, c in enumerate(str(counter), start=1):
                        chars.insert(i + j, c)
                    counter = 1
        return len(chars)

    def compress_2(self, chars: list[str]) -> int:
        """Using separate list for storing results.

        Time complexity: O(N)
        Space complexity: O(N)
        """
        comp = [chars[0]]
        group_counter = 0

        for c in chars:
            if comp[-1] != c:
                if group_counter > 1:
                    comp.append(group_counter)
                comp.append(c)
                group_counter = 0
            group_counter += 1

        if group_counter > 1:
            comp.append(group_counter)
        comp_str = "".join(map(str, comp))
        return len(comp_str)


if __name__ == "__main__":
    solution = Solution()
    inputs = [
        ["a", "a", "b", "b", "c", "c", "c"],
        ["a"],
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
        ["a", "a", "a", "b", "b", "a", "a"],
    ]
    expected = [6, 1, 4, 6]

    funcs = [
        solution.compress,
        solution.compress_2,
    ]
    for f, input, expect in (
        (f, i, e) for i, e in zip(inputs, expected) for f in funcs
    ):
        print(f"\nRunning {f.__name__}")
        for input, expect in zip(inputs, expected):
            output = f(input)
            assert output == expect, f"{input=}, {expect=}, {output=}"
            t = timeit(
                stmt=f"f({input})",
                number=10_000,
                globals=globals(),
            )
            print(f"{f.__name__} took: {t:.6f}")

    print("PASSED!!!")

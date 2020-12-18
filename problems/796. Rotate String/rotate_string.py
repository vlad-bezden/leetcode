class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A * 2


if __name__ == "__main__":
    inputs = [
        ("abcde", "cdeab"),
        ("abcde", "abced"),
        ("Bloomberg", "ergBloomb"),
        ("Bloomberg", "regBloomb"),
    ]
    expected = [True, False, True, False]

    s = Solution()
    for input, expect in zip(inputs, expected):
        output = s.rotateString(*input)
        assert output == expect, f"{input=}, {expect=}, {output=}"

    print("PASSED!!!")

"""Reverse Words in a String II

    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3806/

    Given a character array s, reverse the order of the words.

    A word is defined as a sequence of non-space characters.
    The words in s will be separated by a single space.

    Your code must solve the problem in-place, i.e. without allocating extra space.

    Example 1:

    Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    Example 2:

    Input: s = ["a"]
    Output: ["a"]
"""


class Solution:
    @staticmethod
    def reverseWords(s: list[str]) -> None:
        """
        1. reverse whole sentence (s)
        2. find words that separated by ' ' and swap them
        3. swap last word in the sentence, since it's is not separated by ' ' and
            can't be found
        """

        def swap(start, len) -> None:
            """Swaps characters in the string

            start: start position
            len: how many chars to swap
            """
            # len != end, end is always higher by 1
            end = len - 1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        swap(0, len(s))

        lp = 0
        for rp, v in enumerate(s):
            if v == " ":
                swap(lp, rp)
                lp = rp + 1

        # swap last word
        swap(lp, len(s))


if __name__ == "__main__":
    inputs = (
        (
            ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"],
            ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"],
        ),
        (["a"], ["a"]),
        (["b", "l", "u", "e"], ["b", "l", "u", "e"]),
        (["a", " ", "b"], ["b", " ", "a"]),
    )

    for input, expected in inputs:
        Solution.reverseWords(input)
        assert input == expected, f"{input=}, {expected}"

    print("PASSED!!!")

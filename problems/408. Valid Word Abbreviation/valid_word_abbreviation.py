"""408. Valid Word Abbreviation.

https://leetcode.com/problems/valid-word-abbreviation/
"""


class Solution:
    @staticmethod
    def validWordAbbreviation(word: str, abbr: str) -> bool:
        word_length = len(word)
        word_idx = 0
        num = 0
        for char in abbr:
            if char.isdigit():
                # handle case if '0' in front of digit
                if char == "0" and num == 0:
                    return False
                num = num * 10 + int(char)
            else:
                word_idx += num
                num = 0
                if word_idx >= word_length or word[word_idx] != char:
                    return False
                word_idx += 1
        word_idx += num
        return word_idx == word_length


if __name__ == "__main__":
    inputs = (
        ({"word": "a", "abbr": "2"}, False),
        ({"word": "internationalization", "abbr": "i12iz4n"}, True),
        ({"word": "apple", "abbr": "a2e"}, False),
        ({"word": "substitution", "abbr": "s10n"}, True),
        ({"word": "substitution", "abbr": "sub4u4"}, True),
        ({"word": "substitution", "abbr": "12"}, True),
        ({"word": "substitution", "abbr": "su3i1u2on"}, True),
        ({"word": "substitution", "abbr": "substitution"}, True),
    )

    for input, expected in inputs:
        output = Solution.validWordAbbreviation(**input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

"""1239. Maximum Length of a Concatenated String with Unique Characters

https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
"""


class Solution:
    @staticmethod
    def maxLength(arr: list[str]) -> int:
        # get strings that don't have duplicate chars and convert them to sets
        sets = [s for i in arr if len(s := set(i)) == len(i)]
        # set result with empty set so we always add s1 when we do s1 | s2
        results = [set()]
        # build all unique set permutations and add them to results
        for s1 in sets:
            results.extend([s1 | s2 for s2 in (s2 for s2 in results if not s1 & s2)])
        return len(max(results, key=len))


inputs = (
    (["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"], 16),
    (["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"], 11),  # abxyz, fgh, cde
    (["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"], 16),
    (["a", "abc", "d", "de", "def"], 6),
    (["un", "iq", "ue"], 4),
    (["cha", "r", "act", "ers"], 6),
    (["abc", "cde", "xyz", "klmj"], 10),
    (["abcdefghijklmnopqrstuvwxyz"], 26),
    (["yy", "bkhwmpbiisbldzknpm"], 0),
)

for input, expected in inputs:
    output = Solution.maxLength(input)
    assert output == expected, f"{input=}, {output=}, {expected=}"

print("PASSED!!!")

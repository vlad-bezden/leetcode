"""1268. Search Suggestions System.

https://leetcode.com/problems/search-suggestions-system/
"""

import bisect


class Solution:
    @staticmethod
    def suggestedProducts(products: list[str], search_word: str) -> list[list[str]]:
        word = ""
        products.sort()
        result = []
        lo_index = 0
        for c in search_word:
            word += c
            lo_index = bisect.bisect_left(products, word, lo=lo_index)
            hi_index = min(lo_index + 3, bisect.bisect_right(products, word + "|"))
            result.append(products[lo_index:hi_index])
        return result


if __name__ == "__main__":
    inputs = (
        (
            (["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"),
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        ),
        (
            (["havana"], "havana"),
            [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
        ),
        (
            (["bags", "baggage", "banner", "box", "cloths"], "bags"),
            [
                ["baggage", "bags", "banner"],
                ["baggage", "bags", "banner"],
                ["baggage", "bags"],
                ["bags"],
            ],
        ),
    )

    for input in inputs:
        params, expected = input
        result = Solution.suggestedProducts(*params)
        assert result == expected

    print("PASSED!!!")

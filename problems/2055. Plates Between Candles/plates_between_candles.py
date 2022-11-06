"""2055. Plates Between Candles.

Level: Medium

https://leetcode.com/problems/plates-between-candles/
"""


import bisect

CANDLE = "|"


class Solution:
    @staticmethod
    def platesBetweenCandles(s: str, queries: list[list[int]]) -> list[int]:
        """
        For every query, we should find out the right most candle and left most candle.
        Then we just count the number of plates between left most and right most candles.
        """
        # Fine the candles indexes
        candle_indexes = [i for i, v in enumerate(s) if v == CANDLE]

        answer = []
        for query in queries:
            left, right = query

            # find the left most candles in the query
            left_most_candle = bisect.bisect_left(candle_indexes, left)

            # find the right most candles in the query
            right_most_candle = bisect.bisect_right(candle_indexes, right)

            # if left_most_candle == right_most_candle,
            # it means there is no candle in the query range
            if left_most_candle == right_most_candle:
                answer.append(0)
                continue

            # find the left most candle index in original array
            left_most_candle_idx = candle_indexes[left_most_candle]

            # find the right most candle index in original array
            right_most_candle_idx = candle_indexes[right_most_candle - 1]

            # find the candles count by checking the index in cand_idx
            candles_count = right_most_candle - left_most_candle

            # `r_idx - l_idx + 1`: the number of something between
            # left most and right most candles
            # then minus the number of candles count
            answer.append(
                right_most_candle_idx - left_most_candle_idx + 1 - candles_count
            )

        return answer


if __name__ == "__main__":
    tests = (
        (("**|**|***|", [[2, 5], [5, 9]]), [2, 3]),
        (
            ("***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]),
            [9, 0, 0, 0, 0],
        ),
    )

    for test in tests:
        input, expected = test
        output = Solution.platesBetweenCandles(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

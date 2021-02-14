from functools import lru_cache

INF = float("inf")
MIN = float("-inf")


class Solution:
    @staticmethod
    def minDifficulty(job_difficulty: list[int], days: int) -> int:
        n = len(job_difficulty)
        if n < days:
            return -1

        @lru_cache(None)
        def helper(index: int, days: int):
            if days == 1:
                return max(job_difficulty[index:])

            res = INF
            max_sofar = MIN
            for i in range(index, n - days + 1):
                max_sofar = max(max_sofar, job_difficulty[i])
                res = min(res, max_sofar + helper(i + 1, days - 1))
            return res

        return helper(0, days)


if __name__ == "__main__":
    inputs = [
        [
            [
                976,
                662,
                877,
                135,
                175,
                628,
                856,
                855,
                807,
                769,
                200,
                223,
                527,
                36,
                399,
                409,
                468,
                884,
                229,
                311,
                41,
                350,
                734,
                472,
                480,
                77,
                299,
                821,
                534,
                776,
                965,
                926,
                867,
                45,
                108,
                504,
                468,
                910,
                594,
                355,
                193,
                905,
                211,
                719,
                191,
                961,
                940,
                176,
                737,
                591,
                831,
                22,
                550,
                822,
                840,
                295,
                643,
                1,
                591,
                227,
                345,
                298,
                918,
                561,
                962,
                977,
                871,
                610,
                39,
                247,
                453,
                405,
                306,
                994,
                782,
                395,
                92,
                81,
                956,
                691,
                692,
                395,
                249,
                351,
                342,
                752,
                709,
                521,
                936,
                997,
                651,
                559,
                760,
                796,
                286,
                531,
                187,
                515,
                550,
                470,
                879,
                747,
                3,
                966,
                933,
                696,
                164,
                547,
                278,
                272,
                343,
                552,
                355,
                303,
                15,
                384,
                870,
                85,
                515,
                959,
                168,
                160,
                77,
            ],
            7,
        ],
        [
            [
                186,
                398,
                479,
                206,
                885,
                423,
                805,
                112,
                925,
                656,
                16,
                932,
                740,
                292,
                671,
                360,
            ],
            4,
        ],
        [[6, 5, 4, 3, 2, 1], 2],
        [[6, 5, 4, 3, 2, 1], 3],
        [[9, 9, 9], 4],
        [[1, 1, 1], 3],
        [[7, 1, 7, 1, 7, 1], 2],
        [[7, 1, 7, 1, 7, 1], 3],
        [[7, 1, 7, 1, 7, 1], 4],
        [[7, 1, 7, 1, 7, 1], 5],
        [[7, 1, 7, 1, 7, 1], 6],
        [[11, 111, 22, 222, 33, 333, 44, 444], 6],
    ]
    expected = [2531, 1803, 7, 9, -1, 3, 8, 15, 16, 23, 24, 843]

    for input, expect in zip(inputs, expected):
        output = Solution.minDifficulty(*input)
        assert output == expect, f"{input=}, {expect=}, {output=}"

    print("\nPASSED!!!")

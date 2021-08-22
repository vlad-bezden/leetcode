"""56. Merge Intervals.

    https://leetcode.com/problems/merge-intervals/
"""


class Solution:
    @staticmethod
    def merge(intervals: list[list[int]]) -> list[list[int]]:
        # 1. Sort intervals
        intervals.sort(key=lambda x: x[0])
        answer = [intervals[0]]
        for interval in intervals[1:]:
            # if there is overlap
            if interval[0] <= answer[-1][1]:
                # there is an overlap, merget current and prev intervals
                answer[-1][1] = max(answer[-1][1], interval[1])
            else:
                # no overlaps
                answer.append(interval)
        return answer


if __name__ == "__main__":
    inputs = (
        ([[2, 6], [1, 3], [15, 18], [8, 10]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[5, 10], [3, 7]], [[3, 10]]),
        ([[6, 8], [5, 10]], [[5, 10]]),
    )

    for input, expected in inputs:
        output = Solution.merge(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

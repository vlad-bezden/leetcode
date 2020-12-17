"""253. Meeting Rooms II.

    Using priority queue with min-heap data structure is the
    fastest one. Second is manually keep track of max number of
    used rooms at any time. Using Counter is the slowest one,
    especially when time is specified in 100s of thousands
    (like it's done on leetcode)

    OUTPUT:
        Processing minMeetingRooms
        minMeetingRooms took: 0.027468
        minMeetingRooms took: 0.019725
        minMeetingRooms took: 0.020282
        minMeetingRooms took: 0.019512
        minMeetingRooms took: 0.018873
        minMeetingRooms took: 0.026804
        minMeetingRooms took: 0.026992
        minMeetingRooms took: 0.053050

        Processing minMeetingRooms_2
        minMeetingRooms_2 took: 0.014512
        minMeetingRooms_2 took: 0.010938
        minMeetingRooms_2 took: 0.011039
        minMeetingRooms_2 took: 0.011412
        minMeetingRooms_2 took: 0.010854
        minMeetingRooms_2 took: 0.014319
        minMeetingRooms_2 took: 0.014524
        minMeetingRooms_2 took: 0.023386

        Processing minMeetingRooms_3
        minMeetingRooms_3 took: 0.107781
        minMeetingRooms_3 took: 0.059678
        minMeetingRooms_3 took: 0.079664
        minMeetingRooms_3 took: 0.079297
        minMeetingRooms_3 took: 0.065631
        minMeetingRooms_3 took: 0.092589
        minMeetingRooms_3 took: 0.094642
        minMeetingRooms_3 took: 0.177556
"""
from collections import Counter
import heapq
from timeit import timeit


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        """Keeps track of max rooms at any point of time.

        The "s" and "e" is very important, so it can be propely sorted.
        End must be before end for the same end and start time ([0, 5][5, 10])
        """
        if not intervals:
            return 0
        START = "s"
        END = "e"
        max_rooms = 0
        curr_rooms = 0
        events = []

        for start, end in intervals:
            events.append((start, START))
            events.append((end, END))
        events.sort()

        for event in events:
            if event[1] == START:
                curr_rooms += 1
            else:
                curr_rooms -= 1
            max_rooms = max(max_rooms, curr_rooms)
        return max_rooms

    def minMeetingRooms_2(self, intervals: list[list[int]]) -> int:
        """Using priority queue of the Min-Heap DS."""
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        h = [intervals[0][1]]
        for interval in intervals[1:]:
            if h[0] <= interval[0]:
                # update the ending time for current room
                heapq.heapreplace(h, interval[1])
            else:
                # add a new room
                heapq.heappush(h, interval[1])
        return len(h)

    def minMeetingRooms_3(self, intervals: list[list[int]]) -> int:
        """Using Counter to find an hour with the max rooms occupied.

        It only works for small number of hours. In leetcode failed because
        time limit excceded. They use number more than 100K.
        For small number like 24 hours it works fine.
        """
        if not intervals:
            return 0
        schedule = Counter()

        for start, end in intervals:
            schedule.update(range(start, end))
        return schedule.most_common(1)[0][1]


if __name__ == "__main__":
    solution = Solution()

    inputs = [
        [[0, 30], [5, 10], [15, 20]],
        [[7, 10], [2, 4]],
        [[0, 15], [5, 10]],
        [[0, 10], [5, 15]],
        [[0, 5], [5, 10]],
        [[0, 5], [0, 10], [5, 10]],
        [[0, 4], [0, 10], [5, 10]],
        [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]],
    ]
    expected = [2, 1, 2, 2, 1, 2, 2, 4]

    funcs = [
        solution.minMeetingRooms,
        solution.minMeetingRooms_2,
        solution.minMeetingRooms_3,
    ]
    for f in funcs:
        print(f"\nProcessing {f.__name__:<15}")
        for input, expect in zip(inputs, expected):
            output = f(input)
            assert output == expect, f"{input=}, {expect=}, {output=}"
            t = timeit(
                stmt=f"f({input})",
                number=10_000,
                globals=globals(),
            )
            print(f"{f.__name__} took: {t:.6f}")

    print("\nPASSED!!!")

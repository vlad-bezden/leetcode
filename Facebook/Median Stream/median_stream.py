"""Median Stream

Using bisect is much faster:

median_stream_bisect took: 0.2024
median_stream_heap took: 0.9315
median_stream_bisect took: 0.1286
median_stream_heap took: 0.2113
median_stream_bisect took: 0.2948
median_stream_heap took: 1.6916

"""

from bisect import insort_right
import heapq
from timeit import timeit


def median_stream_bisect(arr):
    """Using bisect (sorted list)"""
    sorted_list = [arr[0]]
    output = [arr[0]]
    for i, v in enumerate(arr[1:], start=2):
        insort_right(sorted_list, v)
        index = i // 2
        output.append(
            sorted_list[index]
            if i % 2
            else sum(sorted_list[index - 1 : index + 1]) // 2
        )
    return output


def median_stream_heap(arr):
    """Using heap"""
    output = [arr[0]]
    heap = [arr[0]]
    for i, v in enumerate(arr[1:], start=2):
        heapq.heappush(heap, v)
        half_queue = heapq.nsmallest(i // 2 + 1, heap)
        output.append(half_queue[-1] if i % 2 else sum(half_queue[-2:]) // 2)
    return output


if __name__ == "__main__":
    inputs = [
        [[5, 15, 1, 3], [5, 10, 5, 4]],
        [[1, 2], [1, 1]],
        [[2, 4, 7, 1, 5, 3], [2, 3, 4, 3, 4, 3]],
    ]

    for input, expected in inputs:
        for f in [median_stream_bisect, median_stream_heap]:
            output = f(input)
            assert output == expected, f"{input=}, {output=}, {expected=}"

            t = timeit(stmt=f"f({input})", number=100_000, globals=globals())
            print(f"{f.__name__} took: {t:.4f}")

    print("PASSED!!!")

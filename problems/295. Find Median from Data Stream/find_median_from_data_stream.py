"""Find Median from Data Stream

MedianFinderBisect took: 1.6334
MedianFinderHeap took: 0.1825

Conclusion:
    Using two heaps is faster than using sorted list
"""

from bisect import insort_right
from heapq import heappush, heappop
from timeit import timeit


class MedianFinderBisect:
    """Using bisect"""

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        insort_right(self.data, num)

    def findMedian(self) -> float:
        mid = len(self.data) // 2
        return (self.data[mid] + self.data[~mid]) / 2


class MedianFinderHeap:
    """
    Two heaps
    One is a max heap that keeps track of the lower half of items
    One is a min heap that keeps track of the upper half of items

    By default min heap is implemented in python
    so we need to multiply item by -1 in smaller heap to make max

    smaller_half: [-1]
    larger_half: [2, 3]

    If uneven use top of smallest half
    If even use top of smallest_half + top of larger half over two
    """

    def __init__(self):
        self.smaller_half = []
        self.larger_half = []

    def addNum(self, num: int) -> None:
        if len(self.smaller_half) == 0 and len(self.larger_half) == 0:
            heappush(self.smaller_half, -num)
        elif num > -self.smaller_half[0]:
            heappush(self.larger_half, num)
        else:
            heappush(self.smaller_half, -num)

        if len(self.smaller_half) > len(self.larger_half) + 1:
            biggest_from_smaller_half = -heappop(self.smaller_half)
            heappush(self.larger_half, biggest_from_smaller_half)
        elif len(self.larger_half) > len(self.smaller_half) + 1:
            smallest_from_larger_half = heappop(self.larger_half)
            heappush(self.smaller_half, -smallest_from_larger_half)

    def findMedian(self) -> float:
        if len(self.smaller_half) == 0 and len(self.larger_half) == 0:
            return 0
        elif len(self.smaller_half) == len(self.larger_half):
            return (self.larger_half[0] + -self.smaller_half[0]) / 2
        elif len(self.smaller_half) > len(self.larger_half):
            return -self.smaller_half[0]
        else:
            return self.larger_half[0]


if __name__ == "__main__":
    for median_finder in [MedianFinderBisect(), MedianFinderHeap()]:
        def run():
            for i in range(1, 1001):
                median = i
                median_finder.addNum(i)
                assert median_finder.findMedian(), median
                median += 0.5

        t = timeit(
            stmt="run()",
            number=100,
            globals=globals(),
        )
        print(f"{median_finder.__class__} took: {t:.4f}")

    print("PASSED!!!")

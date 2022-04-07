"""346. Moving Average from Data Stream.

Level: Easy

https://leetcode.com/problems/moving-average-from-data-stream/
"""

from collections import deque


class MovingAverage:
    def __init__(self, size: int) -> None:
        self.data = deque(maxlen=size)
        self.sum = 0

    def next(self, val: int) -> float:
        cur_size = len(self.data)
        if cur_size == self.data.maxlen:
            dropped_val = self.data.popleft()
            self.sum -= dropped_val
        else:
            cur_size += 1
        self.sum += val
        self.data.append(val)
        return self.sum / cur_size


if __name__ == "__main__":
    import math

    moving_average = MovingAverage(3)
    assert 1 == moving_average.next(1)
    assert 5.5 == moving_average.next(10)
    assert math.isclose(4.66667, moving_average.next(3), rel_tol=1e-5)
    assert 6 == moving_average.next(5)

    print("PASSED!!!")

"""Find Median from Data Stream
    https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3810/
"""
from bisect import insort_right


class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        insort_right(self.nums, num)

    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        return (self.nums[mid] + self.nums[~mid]) / 2


if __name__ == "__main__":
    inputs = (
        ([1, 2], 1.5),
        ([1, 2, 3], 2.0),
    )
    for input, expected in inputs:
        s = MedianFinder()
        for i in input:
            s.addNum(i)
        output = s.findMedian()
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

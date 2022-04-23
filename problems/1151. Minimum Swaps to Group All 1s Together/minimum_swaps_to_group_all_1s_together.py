"""1151. Minimum Swaps to Group All 1's Together.

Level: Medium

https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/


This is a classic sliding window problem. We maintain two pointers, 
left and right.
1. Calculate the total number of ones in the array
2. Initialize left to 0
3. Now iterate the right pointer and at each point add to count 
of ones if the item is 1
4. While doing this, if (rp - lp), which is number of elements in 
the window) ever exceeds the total number of ones, then we have 
to move left pointer as well. In this case before moving, subtract
from count of ones, the value of the current left pointer position.
5. Update max number of ones found at each stage.
6. Now finally the total number of swaps will be the difference between 
total ones and the max number of ones found so far.
"""


class Solution:
    @staticmethod
    def minSwaps(data: list[int]) -> int:
        total_ones = sum(data)
        if total_ones <= 1:
            return 0
        max_seen_ones = 0  # max ones in a window of length ones [i:i+ones]
        current_seen_ones = sum(data[:total_ones])

        for rp, rv in enumerate(data[total_ones:], start=total_ones):
            max_seen_ones = max(max_seen_ones, current_seen_ones)
            current_seen_ones += rv
            current_seen_ones -= data[rp - total_ones]

        return total_ones - max(max_seen_ones, current_seen_ones)


if __name__ == "__main__":
    tests = (
        ([1, 0, 1, 0, 1], 1),
        ([0, 0, 0, 1, 0], 0),
        ([0, 0], 0),
        ([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1], 3),
    )

    for test in tests:
        input, expected = test
        result = Solution.minSwaps(input)
        assert result == expected

    print("PASSED!!!")

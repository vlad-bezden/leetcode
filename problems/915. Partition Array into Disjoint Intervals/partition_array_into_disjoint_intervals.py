"""Partition Array into Disjoint Intervals.

    https://leetcode.com/problems/partition-array-into-disjoint-intervals/
    
    Logic:
    Example : [5, 0, 3, 8, 4, 6, 11, 10, 9]
    * At index 4 (val 8) update cur_max to 8 but since the the target is 5
    do not add it or consider this element to add to the left list.
    * At index 5 (val 4), since the value is less than target (5)
    add this to the left list and update the target to cur_max (8)
    This means going forward all the values which are less than 8 we need
    to add in the left list.
    * At index 6 (val 6), since the value is less than new target (8),
    we add this to the left list
"""


class Solution:
    @staticmethod
    def partitionDisjoint(nums: list[int]) -> int:
        target = cur_max = nums[0]
        left_size = 1
        for i, v in enumerate(nums[1:], start=2):
            if v < target:
                left_size = i
                target = cur_max
            cur_max = max(cur_max, v)
        return left_size


if __name__ == "__main__":
    inputs = (
        ([5, 0, 3, 8, 6], 3),
        ([1, 1, 1, 0, 6, 12], 4),
        ([1, 0, 1, 1], 2),
        ([1, 1, 1, 1], 1),
        ([1, 1, 1, 4], 1),
        ([1, 1], 1),
        ([1, 2], 1),
        ([5, 0, 3, 8, 4, 6, 11, 10, 9], 6),
    )

    for input, expected in inputs:
        output = Solution.partitionDisjoint(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

"""1710. Maximum Units on a Truck.

Level: Easy

https://leetcode.com/problems/maximum-units-on-a-truck/
"""


class Solution:
    @staticmethod
    def maximumUnits(box_types: list[list[int]], truck_size: int) -> int:
        box_types.sort(key=lambda x: x[1], reverse=True)
        total_units = 0

        for boxes, units in box_types:
            fit_boxes = min(boxes, truck_size)
            total_units += fit_boxes * units
            truck_size -= fit_boxes

        return total_units


if __name__ == "__main__":
    tests = (
        (([[1, 3], [2, 2], [3, 1]], 4), 8),
        (([[5, 10], [2, 5], [4, 7], [3, 9]], 10), 91),
    )

    for test in tests:
        input, expected = test
        result = Solution.maximumUnits(*input)
        assert result == expected

    print("PASSED!!!")

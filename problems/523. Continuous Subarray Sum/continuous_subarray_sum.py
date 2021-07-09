"""523. Continuous Subarray Sum"""


class Solution:
    @staticmethod
    def checkSubarraySum(nums: list[int], k: int) -> bool:
        reminder = 0
        # reminder 0 at position 0
        reminders_map = {0: 0}
        for i, v in enumerate(nums, start=1):
            reminder = (reminder + v) % k
            # check if reminder is in map
            if (reminder_idx := reminders_map.get(reminder)) is not None:
                # check if reminder is at least 2 consecutive numbers
                if i - reminder_idx >= 2:
                    return True
            # there is no reminder in the map
            else:
                reminders_map[reminder] = i
        return False


if __name__ == "__main__":
    inputs = (
        (([23, 2, 4, 6, 7], 6), True),
        (([23, 2, 6, 4, 7], 6), True),
        (([23, 2, 6, 4, 7], 13), False),
        (([6, 6, 6], 6), True),
        (([5, 4, 2, 8], 6), True),
    )

    for input, expected in inputs:
        output = Solution.checkSubarraySum(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

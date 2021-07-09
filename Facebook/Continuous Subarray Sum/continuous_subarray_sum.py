from collections import deque


def check_subarray_sum(nums: list[int], k: int) -> bool:
    """Checks if there is a subarray in the array that sums to the k.

    Logic: keep track of current sum in current_sum and previous values
    in the queue. If any value in the list greater than k value reset
    all values and start from beggining.
    If current sum is greater than k value remove items from the
    queue and subtract that value from the current_value
    """
    current_sum = 0
    queue = deque()

    for v in nums:
        # if value is greater than k reset all counters
        if v >= k:
            current_sum = 0
            queue.clear()
        else:
            current_sum += v
            while current_sum > k and queue:
                current_sum -= queue.pop()
            if current_sum == k:
                return True
            # current value is less than k, add it to the queue
            queue.appendleft(v)
    return False


if __name__ == "__main__":
    inputs = (
        ([1, 3, 1, 4, 23], 8, True),
        ([6, 3, 1, 3, 1, 23], 8, True),
        ([1, 3, 1, 4, 23], 7, False),
        ([2, 1, 6, 8, 10], 8, False),
        ([2, 1, 6, 1, 10], 8, True),
        ([8], 8, False),
        ([8, 8], 8, False),
    )

    for *input, expected in inputs:
        output = check_subarray_sum(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

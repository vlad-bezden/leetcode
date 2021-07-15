"""560. Subarray Sum Equals K

    https://leetcode.com/problems/subarray-sum-equals-k/
"""
from collections import deque


class Solution:
    @staticmethod
    def subarraySum(nums: list[int], k: int) -> int:
        # current_sum = 0
        # queue = deque()
        # answer = 0

        # for v in nums:
        #     if v >= k:
        #         if v == k:
        #             answer += 1
        #         current_sum = 0
        #         queue.clear()
        #     else:
        #         current_sum += v
        #         if current_sum == k:
        #             answer += 1
        #             current_sum -= queue.popleft()
        #         queue.append(v)

        # return answer
        from collections import defaultdict  # Dictionary that returns a default value for non-existing keys.
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        ans = 0
        count = defaultdict(int)  # Maintain a count of each sum obtained so far. This "defaultdict" returns "0" by default.
        count[0] = 1  # Initial sum of "0" encountered once at the beginning.
        for i in range(len(nums)):
            ans += count[nums[i] - k]  # Add the count of "nums[i] - k" encountered till now.
            count[nums[i]] += 1  # Increment the count of the current sum "nums[i]".
        return ans

if __name__ == "__main__":
    inputs = (
        # (([1, 1, 1], 2), 2),
        # (([1, 2, 3], 3), 2),
        # (([0], 0), 1),
        (([1, 3, 1, 4, 4, 2, 1, 1, 2], 4), 6),
        (([1, -1, 1, -1, 1, -1], 0), 4),
    )

    for input, expected in inputs:
        output = Solution.subarraySum(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

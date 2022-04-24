"""907. Sum of Subarray Minimums.

Level: Medium

https://leetcode.com/problems/sum-of-subarray-minimums/

Explanation: https://leetcode.com/problems/sum-of-subarray-minimums/discuss/257811/Python-O(n)-slightly-easier-to-grasp-solution-(explained)
"""


class Solution:
    @staticmethod
    def sumSubarrayMins(arr: list[int]) -> int:
        arr = [0] + arr
        result = [0] * len(arr)
        stack = [(0, 0)]
        for i, v in enumerate(arr):
            while stack[-1][1] > v:
                stack.pop()
            j = stack[-1][0]
            result[i] = result[j] + (i - j) * v
            stack.append((i, v))
        return sum(result) % (10**9 + 7)


if __name__ == "__main__":
    tests = (([3, 1, 2, 4], 17), ([11, 81, 94, 43, 3], 444))
    for test in tests:
        input, expected = test
        result = Solution.sumSubarrayMins(input)
        assert result == expected

    print("PASSED!!!")

"""1539. Kth Missing Positive Number.

https://leetcode.com/problems/kth-missing-positive-number/
"""


class Solution:
    @staticmethod
    def findKthPositive(arr: list[int], k: int) -> int:
        if k <= arr[0] - 1:
            return k
        k -= arr[0] - 1
        for i, v in enumerate(arr[:-1]):
            # missing between arr[i] and arr[i + 1]
            current_missing = arr[i + 1] - v - 1
            # if the kth missing is between
            if k <= current_missing:
                return v + k
            # otherwise, proceed further
            k -= current_missing

        # if the missing number is greater than arr[-1]
        return arr[-1] + k


if __name__ == "__main__":
    inputs = ((([2, 3, 4, 7, 11], 5), 9), (([1, 2, 3, 4], 2), 6))
    for input, expected in inputs:
        output = Solution.findKthPositive(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

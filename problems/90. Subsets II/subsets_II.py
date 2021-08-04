"""90. Subsets II.

    https://leetcode.com/problems/subsets-ii/
"""


class Solution:
    @staticmethod
    def subsetsWithDup(nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        length = len(nums)

        def helper(index, sublist):
            ans.append(sublist)
            # base case
            if index >= length:
                return
            seen = set()
            for i, v in enumerate(nums[index:], start=index):
                if v not in seen:
                    seen.add(v)
                    helper(i + 1, sublist + [v])

        helper(0, [])
        return ans


if __name__ == "__main__":
    inputs = (
        ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
        ([0], [[], [0]]),
        ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
        (
            [4, 4, 4, 1, 4],
            [
                [],
                [1],
                [1, 4],
                [1, 4, 4],
                [1, 4, 4, 4],
                [1, 4, 4, 4, 4],
                [4],
                [4, 4],
                [4, 4, 4],
                [4, 4, 4, 4],
            ],
        ),
    )

    for input, expected in inputs:
        output = Solution.subsetsWithDup(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

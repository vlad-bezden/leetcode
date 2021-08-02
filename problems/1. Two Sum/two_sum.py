"""1. Two Sum

    https://leetcode.com/problems/two-sum/
"""


class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        hash = {}
        for i, v in enumerate(nums):
            if (i2 := hash.get(target - v)) is not None:
                return [i2, i]
            hash[v] = i
        return nums


if __name__ == "__main__":
    inputs = (
        ({"nums": [2, 7, 11, 15], "target": 9}, [0, 1]),
        ({"nums": [3, 2, 4], "target": 6}, [1, 2]),
        ({"nums": [3, 3], "target": 6}, [0, 1]),
    )
    for input, expected in inputs:
        output = Solution.twoSum(**input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

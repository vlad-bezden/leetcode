from typing import Optional


class Solution:
    def twoSum(self, nums: list[int], target: int) -> Optional[list[int]]:
        hash: dict[int, int] = {}
        for i, v in enumerate(nums):
            if (i2 := hash.get(target - v)) is not None:
                return [i2, i]
            hash[v] = i
        return None


if __name__ == "__main__":
    solution = Solution()

    input = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    output = solution.twoSum(input, target)
    assert output == expected, f"{expected=}, {output=}"

    input = [3, 2, 4]
    target = 6
    expected = [1, 2]
    output = solution.twoSum(input, target)
    assert output == expected, f"{expected=}, {output=}"

    input = [3, 3]
    target = 6
    expected = [0, 1]
    output = solution.twoSum(input, target)
    assert output == expected, f"{expected=}, {output=}"

    print("PASSED!!!")

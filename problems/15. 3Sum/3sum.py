"""15. 3Sum."""


class Solution:
    @staticmethod
    def threeSum(nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        answers = set()
        for i, v in enumerate(nums[:-2]):
            if v > 0:
                break
            lp = i + 1
            rp = n - 1
            while lp < rp:
                lpv, rpv = nums[lp], nums[rp]
                sum_ = v + rpv + lpv
                if sum_ == 0:
                    answers.add((v, lpv, rpv))
                    lp += 1
                    rp -= 1
                elif sum_ > 0:
                    rp -= 1
                else:
                    lp += 1
        return list(answers)


if __name__ == "__main__":
    inputs = (
        ([-1, 0, 1, 2, -1, -4], [(-1, 0, 1), (-1, -1, 2)]),
        ([], []),
        ([0], []),
        ([-4, 2, 2, 6, 8, 4, 0], [(-4, 0, 4), (-4, 2, 2)]),
        ([0, 0, 0], [(0, 0, 0)]),
        ([3, -2, -1], [(-2, -1, 3)]),
        (
            [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],
            [
                (-3, -1, 4),
                (-1, 0, 1),
                (-4, 1, 3),
                (-2, 0, 2),
                (-1, -1, 2),
                (-3, 0, 3),
                (-4, 0, 4),
                (-2, -1, 3),
                (-3, 1, 2),
            ],
        ),
        ([-2, 0, 0, 2, 2], [(-2, 0, 2)]),
    )
    for input, expected in inputs:
        output = Solution.threeSum(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

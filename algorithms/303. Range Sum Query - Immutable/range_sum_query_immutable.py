class NumArray:
    def __init__(self, nums: list[int]) -> None:
        self._nums = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            self._nums[i + 1] = self._nums[i] + n

    def sumRange(self, i: int, j: int) -> int:
        return self._nums[j + 1] - self._nums[i]


if __name__ == "__main__":
    s = NumArray([-2, 0, 3, -5, 2, -1])
    assert s.sumRange(0, 2) == 1
    assert s.sumRange(2, 5) == -1
    assert s.sumRange(0, 5) == -3

    print("PASSED!!!")

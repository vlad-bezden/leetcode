from __future__ import annotations


class SparseVector:
    def __init__(self, nums: list[int]) -> None:
        # reversed map (index: value)
        self.map = {i: v for i, v in enumerate(nums) if v}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: SparseVector) -> int:
        # find shortest dict
        f, s = (
            (self.map, vec.map) if len(self.map) < len(vec.map) else (vec.map, self.map)
        )
        return sum(v * s.get(i, 0) for i, v in f.items())


if __name__ == "__main__":
    inputs = [
        [[1, 0, 0, 2, 3], [0, 3, 0, 4, 0], 8],
        [[0, 1, 0, 0, 0], [0, 0, 0, 0, 2], 0],
        [[0, 1, 0, 0, 2, 0, 0], [1, 0, 0, 0, 3, 0, 4], 6],
        [[0], [0], 0],
        [[1], [0], 0],
    ]

    for nums1, nums2, expected in inputs:
        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        output = v1.dotProduct(v2)
        assert output == expected, f"{nums1=}{nums2}, {output=}, {expected=}"

    print("PASSED!!!")

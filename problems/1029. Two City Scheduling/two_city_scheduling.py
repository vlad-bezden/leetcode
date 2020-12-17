"""1029. Two City Scheduling."""


class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        half = len(costs) // 2
        return sum(c[0] if i < half else c[1] for i, c in enumerate(costs))


if __name__ == "__main__":
    inputs = [
        [[10, 20], [30, 200], [400, 50], [30, 20]],
        [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]],
        [
            [515, 563],
            [451, 713],
            [537, 709],
            [343, 819],
            [855, 779],
            [457, 60],
            [650, 359],
            [631, 42],
        ],
    ]
    expected = [110, 1859, 3086]

    solution = Solution()
    for input, expect in zip(inputs, expected):
        output = solution.twoCitySchedCost(input)
        assert output == expect, f"{expect=}, {output=}"

    print("\nPASSED!!!")

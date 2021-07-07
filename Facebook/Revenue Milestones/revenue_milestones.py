from bisect import bisect_right
from itertools import accumulate


def get_milestone_days(revenues: list[int], milestones: list[int]) -> list[int]:
    milestones_map = {m: i for i, m in enumerate(milestones)}
    milestones.sort()
    milestone = 0
    output = [-1] * len(milestones)
    for day, revenue in enumerate(accumulate(revenues), start=1):
        rp = bisect_right(milestones, revenue)
        for k in milestones[milestone:rp]:
            output[milestones_map[k]] = day
        milestone = rp
    return output


if __name__ == "__main__":
    inputs = [
        [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [100, 200, 500], [4, 6, 10]],
        [[100, 200, 300, 400, 500], [300, 800, 1000, 1400], [2, 4, 4, 5]],
        [
            [700, 800, 600, 400, 600, 700],
            [3100, 2200, 800, 2100, 1000],
            [5, 4, 2, 3, 2],
        ],
    ]

    for *input, expected in inputs:
        output = get_milestone_days(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")

from operator import itemgetter


def find_positions_list(arr: list[int], x: int) -> list[int]:
    q = [(v, i) for i, v in enumerate(arr, start=1)]
    output = []

    for _ in range(x):
        tmp = q[:x]
        max_item = max(tmp, key=itemgetter(0))
        output.append(max_item[1])
        tmp.remove(max_item)
        # decrement value by 1 for each item unless it's 0
        tmp = [(v - 1, i) if v > 0 else (v, i) for v, i in tmp]
        q = q[x:] + tmp
    return output


if __name__ in "__main__":
    inputs = [
        [[1, 2, 2, 3, 4, 5], 5, [5, 6, 4, 1, 2]],
        [[2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4], 4, [2, 5, 10, 13]],
        [
            [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4],
            13,
            [2, 4, 10, 12, 1, 3, 5, 6, 7, 8, 9, 11, 13],
        ],
    ]

    for *input, expected in inputs:
        output = find_positions_list(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
